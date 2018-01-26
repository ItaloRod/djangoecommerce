#coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True) #Ao criar o modelo, ele seta a data atual
    modified = models.DateTimeField('Modificado em', auto_now=True) # ao ser salvo, ele seta a data atual

    class Meta:
        #classe Meta faz referência a algumas informações da classe ao ser exibida no Admin, como seu nome e outras possibilidades.
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name  # altera o termo Object para o nome do objeto

    def get_absolute_url(self): #retorna a url para a chamada nos templates
        return reverse('catalog:category', kwargs={'slug': self.slug})

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('catalog.Category', verbose_name= 'Categoria')
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    created = models.DateTimeField('Criado em', auto_now_add=True) #Ao criar o modelo, ele seta a data atual
    modified = models.DateTimeField('Modificado em', auto_now=True) # ao ser salvo, ele seta a data atual
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
        
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})