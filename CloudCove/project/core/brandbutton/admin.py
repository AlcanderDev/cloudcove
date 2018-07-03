from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BrandUser

admin.site.register(BrandUser, UserAdmin)