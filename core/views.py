#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
# Reverse_lazy usada quando necessitar usar uma URL
#  antes que as Url's sejam carregadas. é utilizar quando houver um atributo url dentro de uma class-based view genérica
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView, FormView
from django.contrib.auth import get_user_model

from .forms import ContactForm
#view e TemplateView São classes genéricas que auxiliam
# o programador a definir class based-views. View implementa
# dois métodos chamado get e post, quanto templateview é 
# para renderização de templates.

#CreateView é uma view que cria objetos, ela precisa de um modelo para criar, 
# um formulário e renderiza esse formulário para realizar todo o controle

user = get_user_model() #Objeto que recebe o método de obtenção do usuário
class indexView(TemplateView):

    template_name = 'index.html'

index = indexView.as_view()


class contactView(FormView):

    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.send_mail()
            
        return super().form_valid(form)


contact = contactView.as_view()

class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = user
    success_url = reverse_lazy('index')

register = RegisterView.as_view()

# class-based views:
#   def> Significa utilizar classes para a 
#   chamada de requisições em vez de utilizar funções.
#
#   pq usar class?> porque permite a reutilização do código,
#   isso pq uma classe pode ser herdada por outra e pequenas diferenças
#   podem ser aplicadas.  A ideia é pegar comportamentos semelhantes e 
#   coloca-los em uma lógica única e reaproveita o código.

#Generic View 

 

