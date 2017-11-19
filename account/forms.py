from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='姓名', required=True)
    email = forms.EmailField(label='信箱',required=True)
    password1 = forms.CharField(label='密碼',required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(label='確認密碼',required=True, widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email','password',)
        #exclude = ['password',]
