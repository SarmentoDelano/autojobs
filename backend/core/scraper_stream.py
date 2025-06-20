import time
from core.models import Vaga
from apis.vagas import fetch_vagas_jobs
from apis.remoteok import fetch_remoteok_jobs
from apis.infojobs import fetch_infojobs_jobs
from apis.gupy import fetch_gupy_jobs
from apis.programathor import fetch_programathor_jobs
from apis.remotar import fetch_remotar_jobs

def coletar_vagas_stream(busca: str):
    def pause():
        time.sleep(1.2)  # ajuste aqui se quiser mais tempo

    yield f"🔍 Iniciando busca para: {busca}"
    pause()

    sites = [
        ("Remotar", fetch_remotar_jobs),
        #("RemoteOK", fetch_remoteok_jobs),
        #("InfoJobs", fetch_infojobs_jobs),
        ("Gupy", fetch_gupy_jobs),
        #("Vagas.com", fetch_vagas_jobs),
        #("Programathor", fetch_programathor_jobs),
        
    ]

    total = 0

    for nome, fetch_func in sites:
        yield f"🌐 Buscando no {nome}..."
        pause()
        try:
            vagas = fetch_func(busca)
            yield f"✅ {len(vagas)} vagas encontradas no {nome}."
            pause()
            total += len(vagas)

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
        except Exception as e:
            yield f"❌ Erro em {nome}: {str(e)}"
            pause()

    yield f"🎯 Coleta finalizada. Total: {total} vagas."
    pause()
