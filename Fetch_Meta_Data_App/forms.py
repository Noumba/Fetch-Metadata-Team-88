from django import forms


class FileUpload(forms.Form):
    description = forms.CharField(
        label="Enter file description", max_length=50)
    user_file = forms.FileField()
