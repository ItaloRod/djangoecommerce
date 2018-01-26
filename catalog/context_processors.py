#coding=utf-8
from .models import Category

# Context processors serão carregados no momento de renderização da página. 
# Eles serão utilizandos para preencher valores em todos as possíveis
# renderizações das views

# Todo context processor precisa passar como parâmetro a requisição (request) 
# e retornar um dicionário com as informações. 

# De forma bruta é como se ele pudesse tornar esse dicionário com os dados de forma
# global e acessível a todas as páginas que a utilizarão.

def categories(request):
    return{
    'categories': Category.objects.all()
}