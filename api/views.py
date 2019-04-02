from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from liberadas.models import Liberada
from django.http import JsonResponse
from django.db import connection
from django.db.models.query import QuerySet
from .models import listSemana

# Create your views here.
class api_liberadas(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request,semana):
        data = list(Liberada.objects.filter(semana_liberada=semana).values())
        return JsonResponse(data, safe=False)

class api_listLiberada(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT semana_liberada FROM public.liberadas_liberada group by semana_liberada")
            row = cursor.fetchone()
            for r in row:
                print(str(r)[0:4])
                lista = listSemana()
                lista.idsemana = r
                lista.ano = int(str(r)[0:4])
                lista.semana = int(str(r)[4:6])
                lista.link = "http://192.168.10.54:8000/api/liberadas/"+str(r)
                lista.save()
            
        lista = list(listSemana.objects.all().values())
        return JsonResponse(lista, safe=False)
