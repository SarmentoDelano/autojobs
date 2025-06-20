from rest_framework import viewsets
from .models import Vaga
from .serializers import VagaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.scraper import coletar_vagas
from django.http import StreamingHttpResponse
from core.scraper_stream import coletar_vagas_stream
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

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
            total = Vaga.objects.filter(favorita=False).count()
            Vaga.objects.filter(favorita=False).delete()
            return Response({
                "mensagem": f"{total} vagas não favoritas foram removidas."
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "erro": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def stream_coletar_vagas_view(request):
    palavra = request.GET.get("palavra", "").strip()
    if not palavra:
        return StreamingHttpResponse("data: Erro: palavra não fornecida\n\n", content_type='text/event-stream')

    def event_stream():
        for linha in coletar_vagas_stream(palavra):
            yield f"data: {linha}\n\n"

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')



@api_view(['PATCH'])
def favoritar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    vaga.favorita = not vaga.favorita
    vaga.save()
    return Response({
        "mensagem": f"Vaga {'favoritada' if vaga.favorita else 'desfavoritada'}.",
        "favorita": vaga.favorita
    })
