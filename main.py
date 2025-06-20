import sys
import os
import django
from colorama import Fore, Style, init

# Inicia suporte a cores no terminal (Windows)
init(autoreset=True)

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import Vaga
from apis.vagas import fetch_vagas_jobs
from apis.remoteok import fetch_remoteok_jobs
from apis.infojobs import fetch_infojobs_jobs
from apis.gupy import fetch_gupy_jobs
from apis.programathor import fetch_programathor_jobs
from apis.remotar import fetch_remotar_jobs


TOTAL = 0
BUSCA = sys.argv[1] if len(sys.argv) > 1 else "python"  # palavra-chave opcional

def limpar_banco():
    print(f"{Fore.YELLOW}🧹 Limpando banco de dados...")
    Vaga.objects.all().delete()

def salvar_vagas_remoteok():
    global TOTAL
    print(f"{Fore.CYAN}🌐 Buscando vagas no RemoteOK...")
    vagas = fetch_remoteok_jobs(BUSCA)
    print(f"{Fore.GREEN}✅ Encontradas {len(vagas)} vagas no RemoteOK.\n")
    TOTAL += len(vagas)
    for vaga in vagas:
        Vaga.objects.create(
            empresa=vaga.get("empresa"),
            cargo=vaga.get("cargo"),
            descricao=vaga.get("descricao"),
            salario=vaga.get("salario"),
            tags=";".join(vaga.get("tags") or []),
            link=vaga.get("link"),
            encontrado_em="RemoteOK"
        )

def salvar_vagas_infojobs():
    global TOTAL
    print(f"{Fore.CYAN}🌐 Buscando vagas no InfoJobs...")
    vagas = fetch_infojobs_jobs(BUSCA)
    print(f"{Fore.GREEN}✅ Encontradas {len(vagas)} vagas no InfoJobs.\n")
    TOTAL += len(vagas)
    for vaga in vagas:
        Vaga.objects.create(
            empresa=vaga.get("empresa"),
            cargo=vaga.get("cargo"),
            descricao=vaga.get("descricao"),
            salario=vaga.get("salario"),
            tags=";".join(vaga.get("tags") or []),
            link=vaga.get("link"),
            encontrado_em="InfoJobs"
        )

def salvar_vagas_gupy():
    global TOTAL
    print(f"{Fore.CYAN}🌐 Buscando vagas no Gupy...")
    vagas = fetch_gupy_jobs(BUSCA)
    print(f"{Fore.GREEN}✅ Encontradas {len(vagas)} vagas no Gupy.\n")
    TOTAL += len(vagas)
    for vaga in vagas:
        Vaga.objects.create(
            empresa=vaga.get("empresa"),
            cargo=vaga.get("cargo"),
            descricao=vaga.get("descricao"),
            salario=vaga.get("salario"),
            tags=";".join(vaga.get("tags") or []),
            link=vaga.get("link"),
            encontrado_em="Gupy"
        )

def salvar_vagas_vagasdotcom():
    global TOTAL
    print(f"{Fore.CYAN}🌐 Buscando vagas no Vagas.com...")
    vagas = fetch_vagas_jobs(BUSCA)
    print(f"{Fore.GREEN}✅ Encontradas {len(vagas)} vagas no Vagas.com.\n")
    TOTAL += len(vagas)
    for vaga in vagas:
        Vaga.objects.create(
            empresa=vaga.get("empresa"),
            cargo=vaga.get("cargo"),
            descricao=vaga.get("descricao"),
            salario=vaga.get("salario"),
            tags=";".join(vaga.get("tags") or []),
            link=vaga.get("link"),
            encontrado_em="Vagas.com"
        )

def salvar_vagas_programathor():
    global TOTAL
    print(f"{Fore.CYAN}🌐 Buscando vagas no Programathor...")
    vagas = fetch_programathor_jobs(BUSCA)
    print(f"{Fore.GREEN}✅ Encontradas {len(vagas)} vagas no Programathor.\n")
    TOTAL += len(vagas)
    for vaga in vagas:
        Vaga.objects.create(
            empresa=vaga.get("empresa"),
            cargo=vaga.get("cargo"),
            descricao=vaga.get("descricao"),
            salario=vaga.get("salario"),
            tags=";".join(vaga.get("tags") or []),
            link=vaga.get("link"),
            encontrado_em="Programathor"
        )

def salvar_vagas_remotar():
    global TOTAL
    print(f"{Fore.CYAN}🌐 Buscando vagas no Remotar...")
    vagas = fetch_remotar_jobs(BUSCA)
    print(f"{Fore.GREEN}✅ Encontradas {len(vagas)} vagas no Remotar.\n")
    TOTAL += len(vagas)
    for vaga in vagas:
        Vaga.objects.create(
            empresa=vaga.get("empresa"),
            cargo=vaga.get("cargo"),
            descricao=vaga.get("descricao"),
            salario=vaga.get("salario"),
            tags=";".join(vaga.get("tags") or []),
            link=vaga.get("link"),
            encontrado_em="Remotar"
        )

def coletar_todas_as_vagas():
    salvar_vagas_remotar()
    salvar_vagas_infojobs()
    salvar_vagas_gupy()
    salvar_vagas_vagasdotcom()
    salvar_vagas_programathor()
    salvar_vagas_remoteok()

if __name__ == "__main__":
    print(f"{Fore.BLUE}🔍 Palavra-chave de busca: {BUSCA}")
    limpar_banco()
    coletar_todas_as_vagas()
    print(f"{Fore.MAGENTA}🎯 Coleta finalizada! Total de vagas encontradas: {TOTAL}")
