from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.


from .models import UserRequest


@admin.register(UserRequest)
class MyUserRequestAdmin(ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = ('get_user', 'action_time','req_national_id')
    date_hierarchy = 'action_time'
    search_fields = ['user__username','action_time']

    def get_user(self, obj):
        return obj.user.username

    get_user.short_description = 'User'
    get_user.admin_order_field = 'user__username'
