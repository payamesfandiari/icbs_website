# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    # url(
    #     regex=r'^$',
    #     view=views.HistoryView,
    #     name='search'
    # ),
    url(
        regex=r'^history/$',
        view=views.HistoryView.as_view(),
        name='history'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search'
    ),

]
