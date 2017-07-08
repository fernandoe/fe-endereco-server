# -*- coding:utf-8 -*-
import uuid as uuid__

import factory
from faker import Factory

from fe_endereco.models import Endereco

fake = Factory.create('pt_BR')



class EnderecoFactory(factory.django.DjangoModelFactory):
    uuid = uuid__.uuid4()
    entidade = uuid__.uuid4()
    logradouro = fake.street_address()
    cep = fake.building_number()
    numero = fake.building_number()
    complemento = fake.random_digit_not_null_or_empty()
    bairro = fake.city()
    cidade = fake.city()
    estado = 'XX'

    class Meta:
        model = Endereco
