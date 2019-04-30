from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.

class Cidades(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, null=True)
    cep = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.nome

class Distrito(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    semnomeacao = models.IntegerField(null=True)
    sembaixa = models.IntegerField(null=True)
    def __str__(self):
        return self.nome
class Grupo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, related_name="grupo_distrito", null=True)
    semnomeacao = models.IntegerField(null=True)
    sembaixa = models.IntegerField(null=True)
    grupomae = models.IntegerField(null=True)
    def __str__(self):
        return self.nome

class Consultora(models.Model):
    codigo = models.IntegerField(primary_key=True)
    tipo = models.IntegerField(null=True)
    nome = models.CharField(max_length=50)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name="consultora_grupo", null=True)
    endtlogradouro = models.CharField(max_length=10, null=True)
    endlogradouro = models.TextField(null=True)
    endnumero = models.CharField(max_length=50, null=True)
    endcomplemento = models.CharField(max_length=50, null=True)
    bairro = models.CharField(max_length=50, null=True)
    cep = models.CharField(max_length=50, null=True)
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE, related_name="consultora_cidade", null=True)
    setor = models.IntegerField(null=True)
    ddd = models.CharField(max_length=50, null=True)
    telefone1 = models.CharField(max_length=50, null=True)
    telefone2 = models.CharField(max_length=50, null=True)
    celular = models.CharField(max_length=50, null=True)
    semlancamento = models.IntegerField(null=True)
    indicante = models.IntegerField(null=True)
    ultsemativa = models.IntegerField(null=True)
    sembaixa = models.IntegerField(null=True)
    bloqueadosn = models.CharField(max_length=2, null=True)
    def __str__(self):
        return str(self.codigo)+" "+self.nome

