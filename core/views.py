#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.views.generic import View, TemplateView

#view e TemplateView São classes genéricas que auxiliam
# o programador a definir class based-views. View implementa
# dois métodos chamado get e post, quanto templateview é 
# para renderização de templates.


class indexView(TemplateView):

    template_name = 'index.html'

index = indexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True 
    context = {
        'form': form , 
        'success': success,
    }
    return render(request, 'contact.html', context)

#class-based views:
#   def> Significa utilizar classes para a 
#   chamada de requisições em vez de utilizar funções.
#
#   pq usar class?> porque permite a reutilização do código,
#   isso pq uma classe pode ser herdada por outra e pequenas diferenças
#   podem ser aplicadas.  A ideia é pegar comportamentos semelhantes e 
#   coloca-los em uma lógica única e reaproveita o código.

#Generic View

 

