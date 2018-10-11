from django import forms
# fill in custom user info then save it
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.save()

        return user


class WebsitePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'landing_image',
                  'screenshot_1', 'screenshot_2', 'screenshot_3', 'screenshot_4', 'description', 'site_link')


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ['location']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'is_judge', 'is_pro', 'is_chief', 'is_tribe']
        list_display = []


class RatePostForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['user', 'post']
