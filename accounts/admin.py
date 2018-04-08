# -*- coding=utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):

    list_display = ['username', 'name', 'email','is_active', 'is_staff', 'date_joined'] #campos a serem adicionados a serem listados 

admin.site.register(User, UserAdmin)