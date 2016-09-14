
from django.forms import ModelForm
from django.contrib.admin import widgets

from .models import Applicator


class ApplicatorForm(ModelForm):
    class Meta:
        model = Applicator
        exclude = ('set_date','date_has_been_set',)
        widgets = {
            'request_date' : widgets.AdminSplitDateTime(),
        }
