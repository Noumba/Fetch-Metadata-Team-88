from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserProfile, UserFiles


class FileUpload(forms.Form):
    # description = forms.CharField(
    # label="Enter file description", max_length=50)
    user_file = forms.FileField(label='Choose a file')
    # class Meta:
    #model = UserFiles
    #fields = ['file_uploaded']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
