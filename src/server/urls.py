from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers

from fe_endereco.views import ServiceCEPAPIView, EnderecoModelViewSet

router = routers.SimpleRouter()
router.register(r'enderecos', EnderecoModelViewSet, base_name="enderecos")

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/enderecos/cep/(?P<cep>[0-9]{8})', ServiceCEPAPIView.as_view(), name='enderecos-cep'),

    url(r'^admin/', admin.site.urls),
]
