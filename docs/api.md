# API


## /api/v1/enderecos/

* *POST*: Cria um novo endereço


## /api/v1/enderecos/[uuid]/

* *GET*: Retorna um endereço existente
* *PATCH*: Atualiza um endereço existente
* *DELETE*: Remove um endereço existente


## /api/v1/enderecos/cep/[cep]

* *GET*: Retorna o endereço do CEP informado


ISSUES:

* Adicionar suporte ao PUT.
* Adicionar um mock para o servico que busca o endereco externamente.