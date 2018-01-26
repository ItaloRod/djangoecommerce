#coding=utf-8

from django.conf.urls import url
from . import views
#url de catalgo que referencia a catalog.views
urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    #grupo de expressões regulares para criação de uma URL amigável parametrizada 
    
    # ([\w_-]+ significa que é espera um qualquer valor alfanumérico (string) com a presença de undeline(_) 
    # e o traço(-) podendo se repetir uma ou mais vezes (+))
 
    #?P<slug> é necessário para nomear o slug passado na url. Isso ajuda a evitar confusão
    #quando for necessário usar um id e um slug ao mesmo tempo.
    url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    url(r'produtos/(?P<slug>[\w_-]+)/$', views.product, name='product')
]