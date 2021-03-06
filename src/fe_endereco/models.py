from django.contrib.auth import get_user_model
from django.db import models
from fe_core.models import UUIDModel, Entity

User = get_user_model()


class Endereco(UUIDModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    entidade = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
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
