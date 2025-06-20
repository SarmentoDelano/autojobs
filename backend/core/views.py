from rest_framework import viewsets
from .models import Vaga
from .serializers import VagaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.scraper import coletar_vagas

class VagaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer


class ColetarVagasAPIView(APIView):
    def post(self, request):
        palavra = request.data.get("palavra", "").strip()
        if not palavra:
            return Response({"erro": "Palavra de busca não fornecida."}, status=400)

        try:
            saida = coletar_vagas(palavra)
            return Response({
                "mensagem": f"Busca por '{palavra}' concluída.",
                "saida": saida
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "erro": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LimparVagasAPIView(APIView):
    def post(self, request):
        try:
            total = Vaga.objects.count()
            Vaga.objects.all().delete()
            return Response({
                "mensagem": f"{total} vagas removidas do banco de dados."
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "erro": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
