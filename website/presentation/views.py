from datetime import datetime

from django.template.loader import render_to_string
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import JsonResponse


from .models import UserRequest
from .forms import SearchForm

from suds import Client

# Create your views here.


event_text = '<br />چک برگشتی : {0}<br />مبلغ : {1}<br />صادره : {2}<br />تاریخ چک : {3}<br />تاریخ برگشت چک : {4}<br />'
event_text_loan = '<br />مقدار کل بدهی : {0}<br />مقدار سود : {1}<br />مقدار سررسید : {2}<br />مقدار معوق : {3}' \
                  '<br />مقدار مشکوک : {4}<br /><br />شعبه : {5}<br />'


class HistoryView(LoginRequiredMixin, ListView):
    template_name = 'presentation/history.html'
    model = UserRequest
    context_object_name = 'history'

    def get_queryset(self):
        return UserRequest.objects.filter(user=self.request.user)


class Search(LoginRequiredMixin, View):
    """ Call the class that handles Inquiry Service Call """

    def get(self, request):
        form = SearchForm()
        params = dict()
        params["search"] = form
        return render(request, 'presentation/search.html', params)

    def post(self, request):
        form = SearchForm(request.POST)
        user = request.user
        if form.is_valid() and user.num_of_requests_used < user.num_of_requests:
            data_getter = GetDataFromInquiry()
            query = form.cleaned_data['query_n_id']
            results = dict()
            try:
                req_obj = UserRequest.objects.filter(req_national_id=query)[0]
                print(req_obj)
                if req_obj:
                    if req_obj.resp_cheque:
                        results['check'] = req_obj.resp_cheque
                    else:
                        results['check'] = None
                    if req_obj.resp_loans:
                        results['loan'] = req_obj.resp_loans
                    else:
                        results['loan'] = None
            except IndexError:
                results = data_getter.getdata(query)

            context = dict()
            if results['check']:
                context['check'] = True
            if results['loan']:
                context['loan'] = True
            user.num_of_requests_used += 1
            user.save()

            databse_obj = UserRequest(user=request.user, req_national_id=query, resp_cheque=results['check'],
                                      resp_loans=results['loan'])
            return_str = render_to_string('presentation/partials/_search_results.html', {'result_types': context})
            databse_obj.save()
            return JsonResponse({'page': return_str, 'data': results,})
        else:
            return JsonResponse({'error': form.errors})


class GetDataFromInquiry:
    def __init__(self, url='http://172.16.5.200:8082/InquiryService.svc?wsdl'):

        self.__URL = url
        self.__CLIENT = Client(self.__URL)
        self.__TRANSLATOR = str.maketrans(u'1234567890', u'۱۲۳۴۵۶۷۸۹۰')

    def format_date(self, date):
        return '{0}/{1}/{2}'.format(date[:4], date[4:6], date[6:])

    def getdata(self, national_id):
        results = dict()
        results['check'] = self.getcheckinfo(national_id)
        results['loan'] = self.getloaninfo(national_id)
        return results

    def getloaninfo(self, national_id):
        try:
            result = self.__CLIENT.service.GetOnlineFullFacilityInfo(national_id)
            json_obj_temp = dict()
            json_obj_temp['title'] = {}
            json_obj_temp['events'] = []
            if result and bool(result['IsErrorHappened']) is False:
                if int(result['TotalAmOriginal']) == 0:
                    json_obj_temp = None
                elif result['TotalAmOriginal'] > 0:
                    json_obj_temp['title'] = {
                        'text': {'headline': '<strong>{0} {1}</strong>'.format(result['Name'], result['LName']),
                                 'text': '<p> تعداد وام های جاری :{0} </p><p>مجموع مبالغ : {1} مقدار اصل تسهیلات {2} و سود {3}</p>'.format(
                                     str(len(result['FacilityInformationItems'][0])).translate(self.__TRANSLATOR),
                                     str(result['TotalAmTashilat']).translate(self.__TRANSLATOR),
                                     str(result['TotalAmOriginal']).translate(self.__TRANSLATOR),
                                     str(result['TotalAmBedehi']).translate(self.__TRANSLATOR)
                                 )}}
                    if len(result['FacilityInformationItems']) > 0:
                        for item in result['FacilityInformationItems'][0]:
                            print(item)
                            event_date = datetime.now()
                            json_obj_temp['events'].append(
                                {'text': dict(
                                    headline='{0} مقدار تسهیلات'.format(
                                        str(item['AmOriginal']).translate(self.__TRANSLATOR)),
                                    text=event_text_loan.format(
                                        str(item['AmBedehiKol']).translate(self.__TRANSLATOR),
                                        str(item['AmBenefit']).translate(self.__TRANSLATOR),
                                        str(item['AmSarResid']).translate(self.__TRANSLATOR),
                                        str(item['AmMoavagh']).translate(self.__TRANSLATOR),
                                        str(item['AmMashkuk']).translate(self.__TRANSLATOR),
                                        str(item['BnkShb']).translate(self.__TRANSLATOR),
                                    )),
                                    'start_date': {'month': event_date.month, 'day': event_date.day,
                                                   'year': event_date.year}
                                })

            else:
                json_obj_temp = None
        except Exception:
            return None

        return json_obj_temp

    def getcheckinfo(self, national_id):
        try:
            result = self.__CLIENT.service.GetOnlineFullCheckInfo(national_id)
            json_obj_temp = dict()
            json_obj_temp['title'] = {}
            json_obj_temp['events'] = []
            if result and bool(result['IsErrorHappened']) is False:
                if int(result['CheckCount']) == 0:
                    json_obj_temp = None
                elif result['CheckCount'] > 0:
                    json_obj_temp['title'] = {'text': {'headline': '<strong>{0}</strong>'.format(result['Name']),
                                                       'text': '<p>{0}چک برگشتی </p><br /><p>{1}کل بدهی</p>'.format(
                                                           str(result['CheckCount']).translate(self.__TRANSLATOR),
                                                           str(result['CheckAmountSum']).translate(self.__TRANSLATOR))}}
                    if len(result['CheckInformationItems']) > 0:
                        for item in result['CheckInformationItems'][0]:
                            print(item)
                            event_date = datetime.strptime(str(item['ReturnedDate']), '%Y-%m-%d %X')
                            json_obj_temp['events'].append(
                                {'text': dict(
                                    headline='{0} چک به شماره'.format(item['NOCHQ'].translate(self.__TRANSLATOR)),
                                    text=event_text.format(
                                        item['IDCHQ'].translate(self.__TRANSLATOR),
                                        item['AMCHQ'],
                                        item['DESC'],
                                        self.format_date(item['DTCHQ'].translate(self.__TRANSLATOR)),
                                        self.format_date(item['BCKDTCHQ'].translate(self.__TRANSLATOR))
                                    )),
                                    'start_date': {'month': event_date.month, 'day': event_date.day,
                                                   'year': event_date.year}
                                })
            else:
                json_obj_temp = None
        except Exception:
            return None

        return json_obj_temp
