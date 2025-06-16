from rest_framework import viewsets
from .models import Vaga
from .serializers import VagaSerializer

class VagaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
