from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile


class FileUpload(forms.Form):
    # description = forms.CharField(
    # label="Enter file description", max_length=50)
    user_file = forms.FileField()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
