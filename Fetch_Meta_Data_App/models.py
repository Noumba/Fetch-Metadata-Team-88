from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Files(models.Model):
    '''File model'''
    file_name = models.CharField(max_length=300)
    file_type = models.CharField(max_length=10)
    file_size = models.IntegerField()
    file_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_uploaded = models.FileField()

    def __str__(self) -> str:
        return self.file_name


class Metadata(models.Model):
    meta_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meta_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
