from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.story_list, name='story_list'),
    url(r'^stories/$', views.story_list, name='story_list'),
    url(r'^storyauthor/(?P<pk>\d+)$', views.StoryListbyAuthorView.as_view(), name='storys_by_author'),
    url(r'^storyauthors/$', views.StoryAuthorListView.as_view(), name='storyauthors'),
    #url(r'^storyauthor/(?P<pk>[0-9]+)/$', views.StoryListbyAuthorView, name='storys_by_author'),
    url(r'^story/(?P<pk>[0-9]+)/$', views.story_detail, name='story_detail'),
    url(r'^story/new/$', views.story_new, name='story_new'),
    url(r'^story/(?P<pk>[0-9]+)/edit/$', views.story_edit, name='story_edit'),
    #url(r'^like/$', views.story_like, name='like'),
    url(r'^like-story/$', views.like_count_story, name='like_count_story'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='cetegory'),
    url(r'^search/$', views.search, name='search'),
    url(r'^helloo/$', views.helloo_world, name='helloo_world'),

]
