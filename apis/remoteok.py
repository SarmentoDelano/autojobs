import requests
import re

def clean_html(raw_html):
    # Remove HTML da descrição (básico)
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', raw_html)

def fetch_remoteok_jobs(keyword=None):
    url = "https://remoteok.io/api"
    try:
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp.raise_for_status()
        data = resp.json()[1:]  # remove metadata

        standardized_jobs = []

        for job in data:
            position = job.get('position') or job.get('title')
            tags = job.get('tags') or []
            description = clean_html(job.get('description', ''))
            salary = job.get('salary') or f"{job.get('salary_min', '')}-{job.get('salary_max', '')}"
            link = job.get('apply_url') or job.get('url')

            # Filtro de keyword (opcional)
            if keyword:
                kw = keyword.lower()
                if (position and kw in position.lower()) or any(kw in (t or '').lower() for t in tags):
                    pass
                else:
                    continue

            job_data = {
                'empresa': job.get('company'),
                'cargo': position,
                'descricao': description,
                'salario': salary if salary != '-' else None,
                'tags': tags,
                'link': link
            }

            standardized_jobs.append(job_data)

        return standardized_jobs

    except Exception as e:
        print(f"[RemoteOK] Erro ao buscar vagas: {e}")
        return []
