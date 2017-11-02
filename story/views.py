from django.shortcuts import render
from .models import Story

def story_list(request):
    return render(request, 'story/story_list.html')
