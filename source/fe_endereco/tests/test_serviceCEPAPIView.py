# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from fe_core.tests.factories import AccessTokenFactory
from rest_framework.test import APIClient


class TestServiceCEPAPIView(TestCase):
    def setUp(self):
        access_token = AccessTokenFactory()
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(access_token.token))

    def test_enderecos_cep_get(self):
        response = self.client.get(reverse('enderecos-cep', kwargs={'cep': '94410480'}))
        results = response.data
        self.assertEqual("Rua Doutor Valter de Azeredo", results.get('logradouro'))
        self.assertEqual("Centro", results.get('bairro'))
        self.assertEqual(u"Viamão", results.get('cidade'))
        self.assertEqual("RS", results.get('estado'))
        self.assertEqual("94410480", results.get('cep'))
        self.assertEqual(5, len(results))

    def test_enderecos_cep_get(self):
        response = self.client.get(reverse('enderecos-cep', kwargs={'cep': '12345678'}))
        self.assertEqual(404, response.status_code)

    def test_enderecos_cep_post(self):
        response = self.client.post(reverse('enderecos-cep', kwargs={'cep': '12345678'}))
        self.assertEqual(405, response.status_code)

    def test_enderecos_cep_put(self):
        response = self.client.put(reverse('enderecos-cep', kwargs={'cep': '12345678'}))
        self.assertEqual(405, response.status_code)

    def test_enderecos_cep_delete(self):
        response = self.client.delete(reverse('enderecos-cep', kwargs={'cep': '12345678'}))
        self.assertEqual(405, response.status_code)

    def test_enderecos_cep_patch(self):
        response = self.client.patch(reverse('enderecos-cep', kwargs={'cep': '12345678'}))
        self.assertEqual(405, response.status_code)
