from django.urls import path
from .views import upload_file, download_metadata, LandingPageView, SignUpPageView, LogOutView, LoginView
from . import views

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing"),
    path('signup/', SignUpPageView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('uploadfile/', views.upload_file, name='uploadfile'),
    path('download', views.download_metadata, name='download_metadata'),
    path('dashboard/', views.DashBoardView.as_view(), name='dashboard'),
    path('export_pdf/', views.export_pdf, name='export_pdf'),
    path('dashboard/', views.save_metadata, name='save_metadata'),
    path('profile/', views.ProfileView.as_view(), name='profile')
]
