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

    url(r'^theme/list/$', views.ThemeList.as_view(),
        name="theme_list"),
    url(r'^theme/(?P<pk>[0-9]+)/$', views.ThemeDetail.as_view(),
        name="theme_detail"),

    url(r'^type/ressource/list/$', views.TypeRessourceList.as_view(),
        name="type_ressource_list"),
    url(r'^type/ressource/(?P<pk>[0-9]+)/$', views.TypeRessourceDetail.as_view(),
        name="type_ressource_detail"),

    url(r'^ressource/list/$', views.RessourceList.as_view(),
        name="ressource_list"),
    url(r'^ressource/(?P<pk>[0-9]+)/$', views.RessourceDetail.as_view(),
        name="ressource_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)