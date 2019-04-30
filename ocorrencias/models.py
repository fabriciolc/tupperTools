from django.db import models
from home.models import Consultora
from datetime import date
from django.utils import timezone

class Ocorrencia_tipo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo
class Status_type(models.Model):
    codigo = models.IntegerField(primary_key=True)
    status  = models.CharField(max_length=100)
    def __str__(self):
        return self.status


class Ocorrencia(models.Model):
    consultora = models.ForeignKey(Consultora, on_delete=models.CASCADE, related_name="ocorrencias_consultora")
    codigo_produto = models.IntegerField()
    numero_nota = models.IntegerField()
    observacao = models.TextField()
    nota = models.FileField(upload_to='ocorrencias/notas', null=True, blank=True)
    status = models.ForeignKey(Status_type, on_delete=models.CASCADE)
    date_created = models.DateField(default=date.today)
    last_updated = models.DateField(auto_now=True)
    ocorrencia = models.ForeignKey(Ocorrencia_tipo, on_delete=models.CASCADE, null=True, blank=True)
    garantia = models.BooleanField(default=False)
    nomeProduto = models.CharField(max_length=100,null=True)
    semanaNota = models.IntegerField(default=0,null=True)
    def __str__(self):
        return (str(self.consultora)+" | "+ str(self.codigo_produto)+" | "+str(self.status))

