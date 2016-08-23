from __future__ import absolute_import, unicode_literals


from django.contrib import admin


from .models import Applicator,Application
# Register your models here.

admin.site.register(Application)
admin.site.register(Applicator)

