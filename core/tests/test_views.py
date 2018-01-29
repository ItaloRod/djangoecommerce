#coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail
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

class ContactViewTestCase(TestCase):

    def setUp(self):
        self.client = Client() 
        self.url = reverse('contact') 
    
    def test_view_ok(self):
        # teste o status_code e o TemplateUser na mesma função
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'contact.html')    

    def test_form_error(self):
        # testa se o formulário está exibindo o erro solicitado
        data = {'name': '', 'message': '', 'email': ''}
        response = self.client.post(self.url,data) #realiza o envio especificando o data
        self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')
   
    def test_form_ok(self):
        #testa se o formulário está enviando os dados
        data = {'name': 'test', 'message': 'test', 'email': 'test@test.com'}
        response = self.client.post(self.url,data)
        self.assertTrue(response.context['success']) #verifica se o contexto da view possui o success
        self.assertEqual(len(mail.outbox), 1) #verifica se possui algum e-mail na caixa de saída
        self.assertEquals(mail.outbox[0].subject, 'Contato do Django E-Commerce') #pega a msg da caixa de saída e verifica seu título