from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^([^\/]+)/$', views.index, name='topics-index'),
    url(r'^([^\/]+)/keywords/$', views.list, name='topics-keywords'),
]
