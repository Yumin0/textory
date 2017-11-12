from django.contrib import admin
from .models import StoryAuthor, Story, Tag

admin.site.register(Story)
admin.site.register(StoryAuthor)
admin.site.register(Tag)
