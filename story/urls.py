from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.story_list, name='story_list'),
]
