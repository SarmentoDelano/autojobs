from django.db import models

class Vaga(models.Model):
    empresa = models.CharField(max_length=255, blank=True, null=True)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    salario = models.CharField(max_length=255, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)  # Ex: "python;django;remoto"
    link = models.URLField(max_length=1000, blank=True, null=True)
    encontrado_em = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.empresa} - {self.cargo}"
