from django.urls import path, include
from django.contrib import admin
from rest_framework_nested import routers

from fe_endereco.views import ServiceCEPAPIView, EnderecoModelViewSet

router = routers.SimpleRouter()
router.register(r'enderecos', EnderecoModelViewSet, base_name="enderecos")

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/enderecos/cep/<int:cep>', ServiceCEPAPIView.as_view(), name='enderecos-cep'),
    path('admin/', admin.site.urls),
    path('version', include('fe_version.urls')),
]
