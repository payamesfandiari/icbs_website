from __future__ import unicode_literals
import datetime


from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Applicator(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام و نام خانوادگی')
    company_name = models.CharField(max_length=200,verbose_name='نام شرکت')
    address = models.CharField(max_length=400,verbose_name='آدرس شرکت')
    city = models.CharField(max_length=50,verbose_name='شهر')
    email = models.EmailField(blank=False,verbose_name='آدرس ایمیل')
    website = models.URLField(blank=True,verbose_name='آدرس وبسایت شرکت')

    def __str__(self):
        return self.company_name


@python_2_unicode_compatible
class Application(models.Model):
    applicator = models.ForeignKey(Applicator)
    request_date = models.DateTimeField()
    set_date = models.DateTimeField(blank=True,null=True)
    date_has_been_set = models.BooleanField(default=False)

    def __str__(self):
        return '{0} -> {1}'.format(self.applicator.company_name,self.request_date)

    class Meta:
        ordering = ['request_date']








