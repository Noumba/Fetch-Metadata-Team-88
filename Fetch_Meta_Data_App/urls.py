from django.urls import path
from .views import upload_file, download_metadata
from . import views

urlpatterns = [
    path('index/', views.upload_file, name='index'),
    path('download', views.download_metadata, name='download_metadata')
]
