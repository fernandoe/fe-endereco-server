# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from fe_core.models import UUIDModel, Entity


class Endereco(UUIDModel):
    entidade = models.ForeignKey(Entity, null=True, blank=True)
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=128)
    numero = models.CharField(max_length=32)
    complemento = models.CharField(max_length=32, null=True, blank=True)
    bairro = models.CharField(max_length=56)
    cidade = models.CharField(max_length=56)
    estado = models.CharField(max_length=2)

    class Meta:
        verbose_name = u'Endereço'
        verbose_name_plural = u'Endereços'
