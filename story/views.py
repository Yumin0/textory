from django.views.generic.list import ListView
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Story, StoryAuthor, Category, ThingAdjective
from .forms import StoryForm
from django.forms import ModelChoiceField
from django.http import HttpResponse
from django.views import generic
#from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


#def story_list(request):
#    return render(request, 'story/story_list.html')
def hello_world(request):
    return render(request, 'story/hello.html',)

def helloo_world(request):
    return render(request, 'story/helloo.html',)

def story_list(request):
    storys = Story.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    #query = request.GET.get("q")
    #if query:
    #    queryset_list = queryset_list.filter(category__icontains=query)
    return render(request, 'story/story_list.html', {'storys':storys})

class StoryListbyAuthorView(generic.ListView):

    """
    Generic class-based view for a list of blogs posted by a particular StoryAuthor.
    """
    model = Story
    template_name = 'story/story_list_by_author.html'

    def get_queryset(self):
        """
        Return list of Story objects created by StoryAuthor (author id specified in URL)
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
    #story_id = request.POST.get('id')
    story_id = story.pk
    liked = False
    if request.session.get('has_liked_'+str(story_id), liked):
        liked = True
        print("liked {}_{}".format(liked, story_id))
    context = {'story':story, 'liked': liked}
    return render(request, 'story/story_detail.html', {'story': story})


def story_new(request):
    if request.method == "POST":
       form = StoryForm(request.POST)
       #form.StoryAuthor = request.user
       if form.is_valid():
           story = form.save(commit=False)
           story.author, _ = StoryAuthor.objects.get_or_create(user=request.user)
           #StoryAuthor = request.user
           story.created_date = timezone.now()
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
            story.created_date = timezone.now()
            story.save()
            return redirect('story_detail', pk=story.pk)
    else:
        form = StoryForm(instance=story)
    return render(request, 'story/story_edit.html', {'form': form})


def like_count_story(request):
    liked = False
    if request.method == 'GET':
        story_id = request.POST.get('id')
        story = Story.objects.get(id=int(story_id))
        if request.session.get('has_liked_'+story_id, liked):
            print("unlike")
            if story.likes > 0:
                likes = story.likes - 1
                try:
                    del request.session['has_liked_'+story_id]
                except KeyError:
                    print("keyerror")
        else:
            print("like")
            request.session['has_liked_'+story_id] = True
            likes = story.likes + 1
    story.likes = likes
    story.save()
    return HttpResponse(likes, liked)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    storys = Story.objects.filter(category=cate)
    return render(request, 'story/story_list.html', {'storys': storys})


class CategoryView(ListView):
    model = Story
    template_name = 'story/story_list.html'
    context_object_name = 'storys'

    #def get_queryset(self):
    #    id = self.kwargs['pk']
    #    p=get_object_or_404(PersonAdjective, pk = id)
    #    return Story.objects.filter(person_adjective=p)
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

def search(request):
    query = request.GET.get('q')
    error_msg = ''

    if not query:
        error_msg = '请输入关键词'
        return render(request, 'story/story_list.html', {'error_msg': error_msg})

    storys = Story.objects.filter(Q(category__icontains=query) | Q(sb_name__icontains=query))
    return render(request, 'story/story_list.html', {'error_msg': error_msg,
                                               'storys': storys})

#@login_required
#@require_POST
#def story_like(request):
#    story_id = request.POST.get('id')
#    action = request.POST.get('action')
#    if story_id and action:
#        try:
#            story = Story.objects.get(id=story_id)
#            if action == 'like':
#                story.users_like.add(request.user)
#            else:
#                story.users_like.remove(request.user)
#            return JsonResponse({'status':'ok'})
#        except:
#            pass
#    return JsonResponse({'status':'ko'})
