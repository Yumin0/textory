from django.contrib import admin
from .models import StoryAuthor, Category, ThingAdjective, Story

admin.site.register(Story)
admin.site.register(StoryAuthor)
admin.site.register(Category)
admin.site.register(ThingAdjective)
