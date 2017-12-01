# coding: utf-8

from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from catalogue import views

urlpatterns = [
    url(r'^$', views.api_root,
        name="root"),

    url(r'^function/list/$', views.FunctionList.as_view(),
        name="function_list"),
    url(r'^function/(?P<pk>[0-9]+)/$', views.FunctionDetail.as_view(),
        name="function_detail"),

    url(r'^person/list/$', views.PersonList.as_view(),
        name="person_list"),
    url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view(),
        name="person_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)