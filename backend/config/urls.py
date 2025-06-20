from core.views import VagaViewSet, ColetarVagasAPIView
from core.views import LimparVagasAPIView
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import VagaViewSet
from core.views import stream_coletar_vagas_view
from core.views import favoritar_vaga


router = routers.DefaultRouter()
router.register(r'vagas', VagaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/coletar-vagas/', ColetarVagasAPIView.as_view(), name='coletar-vagas'),
    path('api/limpar-vagas/', LimparVagasAPIView.as_view(), name='limpar-vagas'),
    path('api/stream-coletar-vagas/', stream_coletar_vagas_view, name='stream-coletar-vagas'),
    path('api/vagas/<int:pk>/favoritar/', favoritar_vaga, name='favoritar-vaga'),

]
