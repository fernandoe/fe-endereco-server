# -*- coding:utf-8 -*-
from django.test import TestCase

from fe_endereco.services import CEP


class TestCEP(TestCase):

    def test_pesquisar(self):
        dados = CEP.pesquisar('91060280')
        self.assertEqual('Rua Doutor Alberto Albertini', dados['logradouro'])
        self.assertEqual(u'São Sebastião', dados['bairro'])
        self.assertEqual('Porto Alegre', dados['cidade'])
        self.assertEqual('RS', dados['estado'])
        self.assertEqual('91060280', dados['cep'])
        self.assertEqual(5, len(dados))

    def test_pesquisar_invalido(self):
        dados = CEP.pesquisar('invalid')
        self.assertIsNone(dados)

    def test_pesquisar_none(self):
        dados = CEP.pesquisar(None)
        self.assertIsNone(dados)
