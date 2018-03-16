from django.db import models
from django.core import validators
import re
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin #bibliotecas específicas para poder trabalhar com os elementos básicos de um modelo de User
# Create your models here.

# é interessante que o programador inicie o projeto implementando a custom user. 
# Não realizar essa operação pode causar conflito com outros relacionamentos.

#AbstractBaseUser > Dá a base para a criação do modelo
#PermissionsMixin > Dá a permissões e grupos de usuário ao novo modelo

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Apelido / Usuário', 
    max_length = 30, unique = True, validators = [
        validators.RegexValidator(
            re.compile('^[\w.@+-]+$'),
            'Informe um nome de usuário válido. Este valore deve conter apenas letras, números e os caracteres: @/ ./ +/ -/ _ .', 'invalid'
        )
    ], help_text = 'Um nome curto que será usado para indentificá-lo de uma forma única na plataforma'
    )
    name = models.CharField('Nome', max_length=100, blank = True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager() # Cria as funções para manutenção do usuário

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username
    
    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(' ')[0]
