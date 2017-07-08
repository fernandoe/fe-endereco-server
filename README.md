# fe-endereco-server

[![Requirements Status](https://requires.io/github/fernandoe/fe-endereco-server/requirements.svg?branch=release%2F0.1.0)](https://requires.io/github/fernandoe/fe-endereco-server/requirements/?branch=release%2F0.1.0)
[![Build Status](https://travis-ci.org/fernandoe/fe-endereco-server.svg?branch=release%2F0.1.0)](https://travis-ci.org/fernandoe/fe-endereco-server)
[![Coverage Status](https://coveralls.io/repos/github/fernandoe/fe-endereco-server/badge.svg?branch=release%2F0.1.0)](https://coveralls.io/github/fernandoe/fe-endereco-server?branch=release%2F0.1.0)

O **fe-endereco-server** é um serviço independente de pesquisa e cadastro de endereços.

# Como usar a aplicação

## Instalação

```bash
git clone git@github.com:fernandoe/fe-endereco-server.git
cd fe-endereco-server
pip install -r requirements/development.txt
```

## Configuração

```bash
python source/manage.py migrate  # Cria o banco de dados - SQLite
python source/manage.py createsuperuser  # Cria um usuário para acessar o Django admin - entre com um email e senha
```

## Rodar a aplicação

```bash
python source/manage.py runserver 0.0.0.0:7002  # Acesse no navegar o endereço http://localhost:7002/admin
```



# Serviços Externos

* https://postmon.com.br

# Stacks

## Produção

* https://endereco.fe.fernandoe.com
