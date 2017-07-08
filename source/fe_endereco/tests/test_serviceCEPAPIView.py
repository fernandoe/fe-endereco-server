# # -*- coding:utf-8 -*-
# from django.core.cache import cache
# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from rest_framework.test import APIClient
#
# from fe_core.tests.factories import TokenFactory
#
#
# class TestServiceCEPAPIView(TestCase):
#
#
#     def setUp(self):
#         token = TokenFactory()
#         cache.set(token.key, token.to_json())
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token.key))
#
#     def test_enderecos_cep_get(self):
#         response = self.client.get(reverse('enderecos-cep',  kwargs={'cep': '94410480'}))
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         results = response.data
#         self.assertEqual("Rua Doutor Valter de Azeredo", results.get('logradouro'))
#         self.assertEqual("Centro", results.get('bairro'))
#         self.assertEqual(u"Viamão", results.get('cidade'))
#         self.assertEqual("RS", results.get('estado'))
#         self.assertEqual("94410480", results.get('cep'))
#         self.assertEqual(5, len(results))
#
#     def test_enderecos_cep_get(self):
#         response = self.client.get(reverse('enderecos-cep', kwargs={'cep': '12345678'}))
#         self.assertEqual(404, response.status_code)
