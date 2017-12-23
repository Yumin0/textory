from django.conf.urls import url
from account import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm

from .views import (
    UserDetailView
)
app_name = 'account'
urlpatterns=[
    #url(r'^$',views.home),
    url(r'^login/$',login, {'template_name': 'account/login.html'}, name='login',),
    url(r'^logout/$',logout,{'template_name': 'account/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, name='password_reset'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    #url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'),
    #url(r'^change-password/$', views.change_password, name='change_password'),﻿
]
