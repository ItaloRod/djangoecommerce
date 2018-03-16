#coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail
from model_mommy import mommy
from django.conf import settings #importação do modelo de User através do Settings 
from django.contrib.auth import get_user_model # Não importar diretamente o model do user com o django.contrib.auth.model import User pois o model pode ter sido customizado.
#reverse informa a url baseada em seu name especificado em url.py
User = get_user_model()
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

class LoginViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user =  mommy.prepare(settings.AUTH_USER_MODEL) # Essa conf. indica qual o modelo que está sendo utilizado como usuário.
        self.user.set_password('123') 
        # Não atribuir direto Self.user.password pois a senha é 
        #armazenada criptografada. Ao usar a função, ele realiza a criptografia da senha utilizada
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_login_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'login.html')
        data = {'username': self.user.username, 'password': '123'}
        response = self.client.post (self.url, data)
        redirect_url = reverse(settings.LOGIN_REDIRECT_URL) # Variável do settings que redireciona a url
        self.assertRedirects(response, redirect_url) #Verifica se o redirecionamento está ok
        self.assertTrue(response.wsgi_request.user.is_authenticated()) #verifica através do Wsgi_request se o usuário está logado

    def test_login_error(self):

        data = {'username': self.user.username, 'password': '1234'}
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'login.html')
        error_msg = ('Por favor, entre com um usuário  e senha corretos. Note que ambos os campos diferenciam maiúsculas e minúsculas.')
        self.assertFormError(response, 'form', None , error_msg) #None indica que ele procurará por non_field errors 

class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('register')

    def tearDown(self):
        self.user.delete()
        
    def test_register_ok(self):
        data = {'username': 'gileno', 'password1': 'teste123', 'password2': 'teste123'}
        response = self.client.post(self.url, data)
        index_url = reverse('index')
        self.assertRedirects(response, index_url)
        self.assertEquals(User.objects.count(), 1)