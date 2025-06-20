from colorama import Fore, init
from core.models import Vaga
import sys
import os

# Adiciona o diretório raiz ao path para importar /apis/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Agora os imports funcionam
from apis.vagas import fetch_vagas_jobs
from apis.remoteok import fetch_remoteok_jobs
from apis.infojobs import fetch_infojobs_jobs
from apis.gupy import fetch_gupy_jobs
from apis.programathor import fetch_programathor_jobs
from apis.remotar import fetch_remotar_jobs


init(autoreset=True)

def coletar_vagas(busca: str) -> str:
    TOTAL = 0
    output = []

    def salvar(nome, vagas):
        nonlocal TOTAL, output
        output.append(f"✅ {len(vagas)} vagas encontradas no {nome}.")
        TOTAL += len(vagas)
        for vaga in vagas:
            Vaga.objects.create(
                empresa=vaga.get("empresa"),
                cargo=vaga.get("cargo"),
                descricao=vaga.get("descricao"),
                salario=vaga.get("salario"),
                tags=";".join(vaga.get("tags") or []),
                link=vaga.get("link"),
                encontrado_em=nome
            )

    output.append(f"🔍 Iniciando busca para '{busca}'...")

    salvar("Remotar", fetch_remotar_jobs(busca))
    #salvar("RemoteOK", fetch_remoteok_jobs(busca))
    salvar("InfoJobs", fetch_infojobs_jobs(busca))
    salvar("Gupy", fetch_gupy_jobs(busca))
    salvar("Vagas.com", fetch_vagas_jobs(busca))
    salvar("Programathor", fetch_programathor_jobs(busca))
    

    output.append(f"🎯 Total de vagas encontradas: {TOTAL}")
    return "\n".join(output)

