from __future__ import unicode_literals


from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _



# Create your models here.
@python_2_unicode_compatible
class Applicator(models.Model):
    name = models.CharField(max_length=200,verbose_name=_('Name'))
    lastname = models.CharField(max_length=200,verbose_name=_('Lastname'))
    company_name = models.CharField(max_length=200,verbose_name=_('Company'))
    phone = models.CharField(max_length=200,verbose_name=_('Phone'))
    address = models.CharField(max_length=400,verbose_name=_('Address'),blank=True)
    city = models.CharField(max_length=50,verbose_name=_('City'),blank=True)
    email = models.EmailField(blank=False,verbose_name=_('Email'))
    website = models.URLField(blank=True,verbose_name=_('Website'))
    rank = models.CharField(max_length=200,verbose_name=_('Rank'))
    request_date = models.DateTimeField()
    set_date = models.DateTimeField(blank=True,null=True)
    date_has_been_set = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Applicator")
        verbose_name_plural = _("Applicators")
        ordering = ("request_date","company_name",)

    def __str__(self):
        return '{0} - {1} -> {2}'.format(self.company_name,self.phone,self.request_date)
