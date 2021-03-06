from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.room_list,
        name='topics-room-list'),
    
    url(r'^([^\/]+)/$',
        views.index,
        name='topics-index'),
    
    url(r'^([^\/]+)/keywords/$',
        views.list,
        name='topics-keywords'),
    
    url(r'^([^\/]+)/keywords/add/$',
        views.add_keyword,
        name='topics-add-keywords'),
]
