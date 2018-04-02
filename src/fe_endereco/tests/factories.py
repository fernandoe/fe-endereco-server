import uuid

import factory
from faker import Factory
from fe_core.factories import EntityFactory

from fe_endereco.models import Endereco

fake = Factory.create('pt_BR')


class EnderecoFactory(factory.django.DjangoModelFactory):
    uuid = factory.Sequence(lambda n: str(uuid.uuid4()))
    entidade = factory.SubFactory(EntityFactory)
    logradouro = fake.street_address()
    cep = fake.building_number()
    numero = fake.building_number()
    complemento = fake.random_digit_not_null_or_empty()
    bairro = fake.city()
    cidade = fake.city()
    estado = 'XX'

    class Meta:
        model = Endereco
