# -*- coding=utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

# Para o admin do Django, é criado dois formulários pois após a criação do usuário ele irá se editar e add mais campos.
class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','name','email']

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','name','is_active','is_staff']
