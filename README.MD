#Django E-Commerce
Projeto realizado em paralelo com as aulas da Udemy

##Iniciando

### Pré-requisitos
Antes de iniciar, verifique se o ambiente de desenvolvimento possui essas ferramentas disponíveis:

* Python 3.6.x ;
* Pip instalado ;
* Python e Pip adicionados como variáveis de ambiente (Caso esteja utilizando o windows) ;
* Banco de dados [PostgreSQL](https://www.postgresql.org/) instalado ;
* Ter instalado o [Virtualenv](https://virtualenv.pypa.io/en/stable/) ; 


### Cofigurando o Virtualenv

Após fazer o clone do projeto rodar o seguinte comando dentro da pasta do projeto para poder criar o env do projeto

````
virtualenv ENV
````

Depois de criado, ative o env chamando o script `activate` no caminho `ENV\Scripts\`:

````
ENV\Scripts\activate
````

Agora, instale as dependências do projeto com:

````
pip install -r requirements.txt
````

### Realizando as migrações as migrações

Antes de fazer as migrações crie um novo banco de dados que irá receber essas migrações:

````SQL
CREATE DATABASE nome_do_seu_banco;
```` 

Faça um arquivo chamado local_settings.py em `\djangocommerce\` com as seguintes configurações:

````python

# coding=utf-8
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nome_do_seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

````
Por padrão a porta utilizada pelo PostgreSQL é a `5432`.

Realize o seguinte comando no CMD\bash:

````
python manage.py migrate
````
Se tudo ocorrer com sucesso, inicie o servidor com:

````
python manage.py runserver
````

## django-Admin

Para ter acesso a um usuário do django admin basta realizar o seguinte comando:

````
python manage.py createsuperuser
````









