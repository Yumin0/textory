from django.views.generic.list import ListView
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Story, StoryAuthor, Tag
from .forms import StoryForm
from django.forms import ModelChoiceField
from django.http import HttpResponse
from django.views import generic
#from django.views.generic import ListView
from django.contrib.auth.models import User

#def story_list(request):
#    return render(request, 'story/story_list.html')
def hello_world(request):
    return render(request, 'story/hello.html',)

def story_list(request):
    storys = Story.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'story/story_list.html', {'storys':storys})

class StoryListbyAuthorView(generic.ListView):

    """
    Generic class-based view for a list of blogs posted by a particular StoryAuthor.
    """
    model = Story
    template_name = 'story/story_list_by_author.html'

    def get_queryset(self):
        """
        Return list of Blog objects created by StoryAuthor (author id specified in URL)
        """
        id = self.kwargs['pk']
        target_author=get_object_or_404(StoryAuthor, pk = id)
        return Story.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        """
        Add StoryAuthor to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(StoryListbyAuthorView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['author'] = get_object_or_404(StoryAuthor, pk = self.kwargs['pk'])
        return context

class StoryAuthorListView(generic.ListView):
    """
    Generic class-based view for a list of bloggers.
    """
    model = StoryAuthor

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)

    return render(request, 'story/story_detail.html', {'story': story})

def story_new(request):
    if request.method == "POST":
       form = StoryForm(request.POST)
       #form.StoryAuthor = request.user
       if form.is_valid():
           story = form.save(commit=False)
           story.author, _ = StoryAuthor.objects.get_or_create(user=request.user)
           #StoryAuthor = request.user
           story.published_date = timezone.now()
           story.tags = save_tagging(request.POST.getlist('tags', []))
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
            StoryAuthor = request.user
            #story.author = request.user
            story.published_date = timezone.now()
            story.save()
            return redirect('story_detail', pk=story.pk)
    else:
        form = StoryForm(instance=story)
    return render(request, 'story/story_edit.html', {'form': form})

def save_tagging(story_getlist_tags):
    cleaned_tags = []
    for value in story_getlist_tags:
        slug = slugify(value)
        if Tag.objects.filter(slug=slug).exists():
            tag = Tag.objects.filter(slug=slug).first()
            cleaned_tags.append(tag)
        else:
            # makesure the slug is not empty string.
            # because I found the empty string is saved.
            if bool(slug.strip()):
                tag = Tag.objects.create(name=value, slug=slug)
                tag.save()
                cleaned_tags.append(tag)
    return cleaned_tags


import json as simplejson
def tag_list(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        tags= Tag.objects.filter(name__icontains = q )[:20]
        results = []
        for tag in tag:
            tag_json = {}
            tag_json['id'] = tag.id
            tag_json['label'] = tag.name
            tag_json['value'] = tag.name
            results.append(tag_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
