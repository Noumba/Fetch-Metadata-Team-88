from django.urls import path
from .views import upload_file, download_metadata, LandingPageView, SignUpPageView, LogOutView, LoginView
from . import views

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing"),
    path('signup/', SignUpPageView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('uploadfile/', views.upload_file, name='uploadfile'),
    path('download', views.download_metadata, name='download_metadata')
]
