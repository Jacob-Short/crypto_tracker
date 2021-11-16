from django.contrib import admin
from authentication.models import User, Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile)