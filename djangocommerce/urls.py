"""djangocommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib.auth.views import login,logout #Login já possui uma view destinada ao login
from django.contrib import admin
from core import views
# o include permite que, ao se deparar com a url produtos 
# ele inclua na total a url de catalog.urls
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^contato/$',views.contact, name='contact'),
    url(r'^entrar/$',login, {'template_name':'login.html'}, name='login'), #Dicionário altera valores padrões dentro da view Como template_name e form utilizados
    url(r'^sair/$',logout, {'next_page':'index'}, name='logout'), 
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^catalogo/',include('catalog.urls', namespace='catalog')),
    url(r'^admin/', admin.site.urls),
]