from django.shortcuts import render
import datetime
# Create your views here.

def current_date(request):
    now = datetime.datetime.now()
    return render(request,'meeting/test.html',context={'current_date':now})
