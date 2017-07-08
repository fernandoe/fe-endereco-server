# # -*- coding:utf-8 -*-
# from django.core.cache import cache
# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APIClient
# 
# from fe_core.tests.factories import TokenFactory
# from fe_endereco.tests.factories import EnderecoFactory
# 
# 
# class TestEnderecoModelViewSet(TestCase):
# 
#     def setUp(self):
#         token = TokenFactory()
#         cache.set(token.key, token.to_json())
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token.key))
#         self.endereco = EnderecoFactory(entidade=token.entidade)
# 
#     def test_get_list(self):
#         response = self.client.get(reverse('enderecos-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
# 
#         result = response.data
#         self.assertEqual(1, result.get('count'))
# 
#         entidade = result.get('results')[0]
#         self.assertTrue('uuid' in entidade)
#         self.assertTrue('created_at' in entidade)
#         self.assertTrue('updated_at' in entidade)
#         self.assertTrue('cep' in entidade)
#         self.assertTrue('logradouro' in entidade)
#         self.assertTrue('numero' in entidade)
#         self.assertTrue('complemento' in entidade)
#         self.assertTrue('bairro' in entidade)
#         self.assertTrue('cidade' in entidade)
#         self.assertTrue('estado' in entidade)
#         self.assertEqual(10, len(entidade))
