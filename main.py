import sys
import os

# Adiciona o diretório backend ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from core.models import Vaga
from apis.remoteok import fetch_remoteok_jobs
from apis.infojobs import fetch_infojobs_jobs
from apis.gupy import fetch_gupy_jobs


def limpar_banco():
    print("Limpando banco de dados...")
    Vaga.objects.all().delete()

def salvar_vagas_remoteok():
    print("Buscando vagas no RemoteOK...")
    vagas = fetch_remoteok_jobs("python")

    for vaga in vagas:
        empresa = vaga.get("empresa")
        cargo = vaga.get("cargo")
        descricao = vaga.get("descricao")
        salario = vaga.get("salario")
        tags = vaga.get("tags")
        link = vaga.get("link")

        tags_str = ";".join(tags) if tags else None

        Vaga.objects.create(
            empresa=empresa,
            cargo=cargo,
            descricao=descricao,
            salario=salario,
            tags=tags_str,
            link=link,
            encontrado_em="RemoteOK"
        )

def salvar_vagas_infojobs():
    print("Buscando vagas no InfoJobs...")
    vagas = fetch_infojobs_jobs("python")

    for vaga in vagas:
        empresa = vaga.get("empresa")
        cargo = vaga.get("cargo")
        descricao = vaga.get("descricao")
        salario = vaga.get("salario")
        tags = vaga.get("tags")
        link = vaga.get("link")

        tags_str = ";".join(tags) if tags else None

        Vaga.objects.create(
            empresa=empresa,
            cargo=cargo,
            descricao=descricao,
            salario=salario,
            tags=tags_str,
            link=link,
            encontrado_em="InfoJobs"
        )

def salvar_vagas_gupy():
    print("Buscando vagas no Gupy...")
    vagas = fetch_gupy_jobs("python")

    for vaga in vagas:
        empresa = vaga.get("empresa")
        cargo = vaga.get("cargo")
        descricao = vaga.get("descricao")
        salario = vaga.get("salario")
        tags = vaga.get("tags")
        link = vaga.get("link")

        tags_str = ";".join(tags) if tags else None

        Vaga.objects.create(
            empresa=empresa,
            cargo=cargo,
            descricao=descricao,
            salario=salario,
            tags=tags_str,
            link=link,
            encontrado_em="Gupy"
        )

def coletar_todas_as_vagas():
    salvar_vagas_remoteok()
    salvar_vagas_infojobs()
    salvar_vagas_gupy()


if __name__ == "__main__":
    limpar_banco()
    coletar_todas_as_vagas()
    print("Coleta finalizada!")
