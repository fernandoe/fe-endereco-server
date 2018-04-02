# -*- coding:utf-8 -*-
from rest_framework import serializers

from .models import Endereco


class EnderecoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = (
            'uuid',
            'created_at',
            'updated_at',
            'cep',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'estado'
        )
        read_only_fields = ('uuid', 'created_at', 'updated_at')
