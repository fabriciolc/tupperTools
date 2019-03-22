from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.

class Grupo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Consultora(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    codigo_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

    
class Status_type(models.Model):
    codigo = models.IntegerField(primary_key=True)
    status  = models.CharField(max_length=100)
    def __str__(self):
        return self.status
