from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.story_list, name='story_list'),
    url(r'^story/(?P<pk>[0-9]+)/$', views.story_detail, name='story_detail'),
    url(r'^story/new/$', views.story_new, name='story_new'),
    url(r'^story/(?P<pk>[0-9]+)/edit/$', views.story_edit, name='story_edit'),
]
