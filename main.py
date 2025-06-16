# from apis.remoteok import fetch_remoteok_jobs

# jobs = fetch_remoteok_jobs("python")
# print("------------------------------------------------------- REMOTEOK -------------------------------------------------------")
# for job in jobs:
#     print("Empresa:", job.get('empresa'))
#     print("Cargo:", job.get('cargo'))
#     print("Descrição:", job.get('descricao'))
#     print("Salário:", job.get('salario'))
#     print("Tags:", ", ".join(job.get('tags', [])))
#     print("Link:", job.get('link'))
#     print("="*50)

from apis.infojobs import fetch_infojobs_jobs

jobs = fetch_infojobs_jobs("python")
print("------------------------------------------------------- INFOJOBS -------------------------------------------------------")
for job in jobs:
    print("Empresa:", job.get('empresa'))
    print("Cargo:", job.get('cargo'))
    print("Descrição:", job.get('descricao'))
    print("Salário:", job.get('salario'))
    print("Tags:", ", ".join(job.get('tags', [])))
    print("Link:", job.get('link'))
    print("="*50)
