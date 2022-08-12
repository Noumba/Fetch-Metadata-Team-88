from django.contrib import admin
from .models import Profile, Files, Metadata
# Register your models here.
admin.site.register(Profile)
admin.site.register(Files)
admin.site.register(Metadata)
