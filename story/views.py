from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Story
from .forms import StoryForm
from django.forms import ModelChoiceField


#def story_list(request):
#    return render(request, 'story/story_list.html')


def story_list(request):
    storys = Story.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'story/story_list.html', {'storys':storys})

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)

    return render(request, 'story/story_detail.html', {'story': story})

def story_new(request):
    if request.method == "POST":
       form = StoryForm(request.POST)

       if form.is_valid():
           story = form.save(commit=False)
           story.author = request.user
           story.published_date = timezone.now()
           story.save()
           return redirect('story_detail', pk=story.pk)
    else:
        form = StoryForm()
    return render(request, 'story/story_create.html', {'form': form})

def story_edit(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == "POST":
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.published_date = timezone.now()
            story.save()
            return redirect('story_detail', pk=story.pk)
    else:
        form = StoryForm(instance=story)
    return render(request, 'story/story_edit.html', {'form': form})
