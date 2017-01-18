__author__ = 'sysmoon'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.app_list, name='app_list'),
    url(r'^app/(?P<pk>[0-9]+)/$', views.app_detail, name='app_detail'),
    url(r'^app/new/$', views.app_new, name='app_new'),
    url(r'^draft/$', views.app_draft_list, name='app_draft_list'),
    url(r'^app/(?P<pk>\d+)/publish/$', views.app_publish, name='app_publish'),
]