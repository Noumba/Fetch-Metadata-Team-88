from django.urls import path
from .views import index, download_metadata
from . import views

urlpatterns = [
    path('index/', index, name='index'),
    path('download', views.download_metadata, name='download')
]
