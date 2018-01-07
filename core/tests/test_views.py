#coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
#reverse informa a url baseada em seu name especificado em url.py

class IndexViewTestCase(TestCase):
    
    #método setUp executado no inicio do teste
    def setUp(self):
        self.client = Client() #Corresponde a um cliente de navegação
        self.url = reverse('index') 
    
    #Executado no fim de cada teste
    def tearDown(self):
        pass

    def test_status_code(self):
        self.response = self.client.get(self.url) #acesso da página inicial pelo método get do client
        self.assertEquals(self.response.status_code, 200) #testa se o status retornado for 200 (sucesso)
    
    def test_template_used(self):
        self.response = self.client.get(self.url)
        self.assertTemplateUsed(self.response, 'index.html') #testa se o template index.html está sendo usado