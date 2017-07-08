# -*- coding:utf-8 -*-
import requests


class CEP(object):
    @staticmethod
    def pesquisar(cep):
        r = requests.get('http://api.postmon.com.br/v1/cep/%s' % cep)
        if r.status_code != 200: return None
        result = r.json()
        return {
            'logradouro': result['logradouro'],
            'bairro': result['bairro'],
            'cep': result['cep'],
            'cidade': result['cidade'],
            'estado': result['estado']
        }
