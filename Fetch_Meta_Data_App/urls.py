from django.urls import path
from .views import upload_file, download_metadata, LandingPageView, SignUpPageView
from . import views

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing"),
    path('signup/', SignUpPageView.as_view(), name='signup')
    #path('index/', views.upload_file, name='upload'),
    #path('download', views.download_metadata, name='download_metadata')
]
