#coding=utf-8

from django.test import TestCase
from model_mommy import mommy
from django.core.urlresolvers import reverse
from catalog.models import Category, Product

class CategoryTestCase(TestCase):

    def setUp(self):
        self.category = mommy.make('catalog.Category') #cria um objeto de produtos
    
    def test_get_absolute_url(self):
        self.assertEqual(self.category.get_absolute_url(),reverse('catalog:category', kwargs={'slug' : self.category.slug}))

class ProductTestCase(TestCase):

    def setUp(self):
        self.product = mommy.make(Product, slug='produto')
        #Funciona dos dois jeitos #você tbm pode passar valores especificos, nesse teste, o slug vai ser produto.
    def test_get_absolute_url(self):
        self.assertEqual(self.product.get_absolute_url(),reverse('catalog:product', kwargs={'slug': 'produto'}))
