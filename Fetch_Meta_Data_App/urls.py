from django.urls import path
from .views import upload_file, download_metadata, LandingPageView, SignUpPageView
from . import views

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing"),
    path('signup/', SignUpPageView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('uploadfile/', views.upload_file, name='uploadfile'),
    path('download', views.download_metadata, name='download_metadata')
]
