from django.shortcuts import render
from django.views.generic import FormView
from .forms import ApplicatorForm

# Create your views here.


class ApplicatorCreate(FormView):
    form_class = ApplicatorForm
    template_name = 'meeting/request_form.html'


    def post(self, request, *args, **kwargs):
        form = ApplicatorForm(request.POST)

