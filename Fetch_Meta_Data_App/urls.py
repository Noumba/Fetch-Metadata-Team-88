from django.urls import path
from .views import upload_file, download_metadata, LandingPageView
from . import views

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing")
    #path('index/', views.upload_file, name='upload'),
    #path('download', views.download_metadata, name='download_metadata')
]
