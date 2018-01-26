#coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from catalog.models import Product, Category
from model_mommy import mommy 

 #exemplo somente do ProductList
class ProductListTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('catalog:product_list')
        self.products = mommy.make('catalog.Product', _quantity=10)
   
    def tearDown(self):
       Product.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        print(response)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)   
        product_list = response.context['products']
        self.assertEquals(product_list.count(), 10) 
        