from django.db import models
from home.models import Consultora
from datetime import date,datetime
from django.utils import timezone
import datetime

# Create your models here.
class Caixa_fabrica(models.Model):
    codigo_caixa = models.TextField(primary_key=True)
    lote = models.IntegerField()
    volume_atual = models.IntegerField()
    volume_total = models.IntegerField()
    distribuicao = models.BigIntegerField()
    rota = models.IntegerField()
    ano = models.IntegerField()
    semana = models.IntegerField()
    consultora = models.IntegerField()
    liberada_status = models.BooleanField(default=False)
    

class Liberada(models.Model):
    #consultora = models.ForeignKey(Consultora, on_delete=models.CASCADE, related_name="liberadas_consultora")
    consultora = models.IntegerField()
    semana = models.IntegerField()
    rota = models.IntegerField()
    volume_total = models.IntegerField()
    volume_atual = models.IntegerField()
    entregador = models.CharField(max_length=50)
    data_liberada = models.DateField(default=date.today)
    semana_liberada = models.IntegerField(default=0)
    caixa_fabrica = models.OneToOneField(Caixa_fabrica, primary_key=True, on_delete=models.CASCADE, related_name="caixa_liberada", unique=True)

    