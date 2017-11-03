from django.conf.urls import url
from account import views
from django.contrib.auth.views import login, logout

app_name = 'account'
urlpatterns=[
    #url(r'^$',views.home),
    url(r'^login/$',login,{'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$',logout,{'template_name': 'account/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    #url(r'^change-password/$', views.change_password, name='change_password'),
]
