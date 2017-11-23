from django.shortcuts import render, redirect
from account.forms import (
    RegistrationForm,
    EditProfileForm
)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from story.models import Story, StoryAuthor
#from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
#def home(request):
    #return render(request, 'account/home.html', args)

User = get_user_model()

class UserDetailView(DetailView):
    model = Story
    template_name = 'account/user_detail.html'
    queryset = User.objects.all()

    #def get_object(self):
    #    return get_object_or_404(
    #                User,
    #                username_iexact=self.kwargs.get("username")
    #                )




def login_redirect(request):
    return redirect('/stories')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/stories')
    else:
        form = RegistrationForm()

        args = {'form':form}
        return render(request,'account/reg_form.html', args)


def view_profile(request):
    args = {'user':request.user}
    storys = Story.objects.all()
    return render(request, 'account/profile.html',args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/edit_profile.html', args)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'account/change_password.html', args)
