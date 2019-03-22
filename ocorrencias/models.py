from django.db import models
from home.models import Consultora,Status_type
from datetime import date
from django.utils import timezone

# Create your models here.
class Ocorrencia(models.Model):
    codigo_consultora = models.ForeignKey(Consultora, on_delete=models.CASCADE)
    codigo_produto = models.IntegerField()
    numero_nota = models.IntegerField()
    ocorrencia = models.TextField(max_length=200)
    observacao = models.TextField()
    nota = models.ImageField(upload_to='ocorrencias/notas', null=True, blank=True)
    status = models.ForeignKey(Status_type, on_delete=models.CASCADE)
    date_created = models.DateField(default=date.today)
    last_updated = models.DateField(auto_now=True)
    def __str__(self):
        return (str(self.codigo_consultora)+" | "+ str(self.codigo_produto)+" | "+str(self.status))
