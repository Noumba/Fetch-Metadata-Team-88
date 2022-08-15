from django.contrib import admin
from .models import UserProfile, Metadata, UserFiles
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserFiles)
admin.site.register(Metadata)


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
# list_display = ['username', 'password', 'email']


# @admin.register(UserPost)
# class PostAdmin(admin.ModelAdmin):
# list_display = ['user', 'file_field']
