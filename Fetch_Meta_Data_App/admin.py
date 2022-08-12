from django.contrib import admin
from .models import Profile, Files, Metadata, User, UserPost
# Register your models here.
# admin.site.register(Profile)
# admin.site.register(Files)
# admin.site.register(Metadata)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'email']


# @admin.register(UserPost)
# class PostAdmin(admin.ModelAdmin):
   # list_display = ['user', 'file_field']
