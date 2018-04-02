from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Endereco
from .serializers import EnderecoModelSerializer
from .services import CEP


class ServiceCEPAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None, *args, **kwargs):
        cep = kwargs.get('cep', None)
        data = CEP.pesquisar(cep)
        if data:
            return Response(data)
        else:
            raise Http404()


class EnderecoModelViewSet(viewsets.ModelViewSet):
    serializer_class = EnderecoModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.entity is None:
            return Endereco.objects.filter(usuario=self.request.user)
        else:
            return Endereco.objects.filter(entidade=self.request.user.entity)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user,
                        entidade=self.request.user.entity)
