from django.urls import reverse
from fe_core.factories import UserFactory, EntityFactory
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from fe_endereco.models import Endereco
from fe_endereco.tests.factories import EnderecoFactory

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class TestEnderecoModelViewSet(APITestCase):
    def setUp(self):
        self.user = UserFactory(entity=None)
        payload = jwt_payload_handler(self.user)
        user_token = jwt_encode_handler(payload)

        self.entity = EntityFactory()
        self.user_with_entity = UserFactory(entity=self.entity)
        payload = jwt_payload_handler(self.user_with_entity)
        self.user_with_entity_token = jwt_encode_handler(payload)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token)

    def test_create_with_only_user(self):
        response = self.client.post(reverse('enderecos-list'), {
            'logradouro': 'a',
            'numero': 1,
            'estado': 'RS',
            'cidade': 'Porto Alegre',
            'bairro': 'b',
            'cep': '91060280'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        endereco = Endereco.objects.get(uuid=response.data['uuid'])
        self.assertIsNone(endereco.entidade)
        self.assertEqual(endereco.usuario, self.user)

    def test_create_with_entity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.user_with_entity_token))
        response = self.client.post(reverse('enderecos-list'), {
            'logradouro': 'a',
            'numero': 1,
            'estado': 'RS',
            'cidade': 'Porto Alegre',
            'bairro': 'b',
            'cep': '91060280'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        endereco = Endereco.objects.get(uuid=response.data['uuid'])
        self.assertEqual(endereco.entidade, self.entity)
        self.assertEqual(endereco.usuario, self.user_with_entity)

    def test_get_with_user(self):
        endereco = EnderecoFactory(usuario=self.user)
        response = self.client.get(reverse('enderecos-detail', kwargs={'pk': str(endereco.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entidade = response.data
        self.assertTrue('uuid' in entidade)
        self.assertTrue('created_at' in entidade)
        self.assertTrue('updated_at' in entidade)
        self.assertTrue('cep' in entidade)
        self.assertTrue('logradouro' in entidade)
        self.assertTrue('numero' in entidade)
        self.assertTrue('complemento' in entidade)
        self.assertTrue('bairro' in entidade)
        self.assertTrue('cidade' in entidade)
        self.assertTrue('estado' in entidade)
        self.assertEqual(10, len(entidade))

    def test_get_with_entity(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.user_with_entity_token))
        endereco = EnderecoFactory(usuario=self.user, entidade=self.entity)
        response = self.client.get(reverse('enderecos-detail', kwargs={'pk': str(endereco.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entidade = response.data
        self.assertTrue('uuid' in entidade)
        self.assertTrue('created_at' in entidade)
        self.assertTrue('updated_at' in entidade)
        self.assertTrue('cep' in entidade)
        self.assertTrue('logradouro' in entidade)
        self.assertTrue('numero' in entidade)
        self.assertTrue('complemento' in entidade)
        self.assertTrue('bairro' in entidade)
        self.assertTrue('cidade' in entidade)
        self.assertTrue('estado' in entidade)
        self.assertEqual(10, len(entidade))

    def test_update_with_user_with_patch(self):
        endereco = EnderecoFactory(usuario=self.user)
        response = self.client.patch(reverse('enderecos-detail', kwargs={'pk': str(endereco.uuid)}), {
            'cidade': 'ABC'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        endereco.refresh_from_db()
        self.assertEqual(endereco.cidade, 'ABC')

    def test_update_with_user_with_put(self):
        endereco = EnderecoFactory(usuario=self.user)
        response = self.client.put(reverse('enderecos-detail', kwargs={'pk': str(endereco.uuid)}), {
            'logradouro': endereco.logradouro,
            'numero': 999,
            'estado': endereco.estado,
            'cidade': endereco.cidade,
            'bairro': endereco.bairro,
            'cep': endereco.cep
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        endereco.refresh_from_db()
        self.assertEqual(endereco.logradouro, response.data['logradouro'])
        self.assertEqual(endereco.numero, response.data['numero'])
        self.assertEqual(endereco.estado, response.data['estado'])
        self.assertEqual(endereco.cidade, response.data['cidade'])
        self.assertEqual(endereco.bairro, response.data['bairro'])
        self.assertEqual(endereco.cep, response.data['cep'])

    def test_delete_with_user(self):
        endereco = EnderecoFactory(usuario=self.user)
        self.assertEqual(1, Endereco.objects.filter(uuid=endereco.uuid).count())
        response = self.client.delete(reverse('enderecos-detail', kwargs={'pk': str(endereco.uuid)}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(0, Endereco.objects.filter(uuid=endereco.uuid).count())
