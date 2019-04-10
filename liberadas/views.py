from django.shortcuts import render
from home.models import Consultora
from .models import Caixa_fabrica,Liberada
from api.models import listSemana
from io import TextIOWrapper
from django.http import JsonResponse
import home.methods as methods
import datetime
from django.db import connection
from threading import Thread
import os, csv


def start_new_thread(function):
    def decorator(*args, **kwargs):
        t = Thread(target = function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator

def form_liberadas(request):
    context = {
        'semana_liberada' : int(datetime.datetime.now().strftime("%Y%V"))-1,
        'titulo' : 'Liberada',
    }
    if request.method == "POST":
        try:
            uploaded_file = request.FILES['fabrica_uploaded_file'].read() # get the uploaded file
            
            salvarCaixas(uploaded_file)
            pass
        except Exception as e:
            print("erro 1")
            print(e)
            pass
        try:
            semana = request.POST.get('semanav')
            csvfile = TextIOWrapper(request.FILES['liberada_uploaded_file'].file)
            salvarLiberada(csvfile, semana)
        except Exception as e:
            print("erro 2")
            print(e)
            pass
    return render(request, 'form_liberada.html', context)
@start_new_thread
def salvarCaixas(file):
    for a in file.splitlines():
        a = a.decode('utf-8')
        codigo_caixa = a[0:18]
        lote = a[18:26]
        volume_atual = a[26:30]
        volume_total = a[30:34]
        distribuicao = a[34:46]
        rota = a[46:50]
        ano = a[50:54]
        semana = a[54:56]
        consultora = a[56:62]
        print(codigo_caixa,lote,volume_atual,volume_total,distribuicao,rota,ano,semana,consultora)
        caixa = Caixa_fabrica()
        caixa.codigo_caixa = str(codigo_caixa)
        caixa.lote = lote
        caixa.volume_atual = volume_atual
        caixa.volume_total = volume_total
        caixa.distribuicao = distribuicao
        caixa.rota = rota
        caixa.ano = ano
        caixa.semana = semana
        caixa.consultora = consultora
        try:
            caixa.save()
        except Exception as e:
            pass
    
@start_new_thread
def salvarLiberada(file,semanaliberada):
    reader = csv.reader(file,delimiter=";")
    count = 0
    for row in reader:
        if methods.is_number(row[3]):
            rota = int(row[0])
            semana = int(row[1])
            totalcaixa = row[2]
            codigo_consultora = int(row[3])
            nome_consultora = row[4]
            entregador = row[5][0:15]
            
            caixa = Caixa_fabrica.objects.filter(consultora=codigo_consultora,semana=semana)

            if not caixa:
                count = count+1
                print(row)
            else:
                for cx in caixa:
                    print(cx)
                    liberada = Liberada()
                    liberada.consultora = cx.consultora
                    liberada.semana = cx.semana
                    liberada.rota = cx.rota
                    liberada.entregador = entregador
                    liberada.volume_atual = cx.volume_atual
                    liberada.volume_total = cx.volume_total
                    liberada.semana_liberada = int(semanaliberada)
                    liberada.caixa_fabrica = cx
                    liberada.save()
                    Caixa_fabrica.objects.filter(codigo_caixa=cx.codigo_caixa).update(liberada_status=True)
                with connection.cursor() as cursor:
                    cursor.execute("SELECT semana_liberada FROM public.liberadas_liberada group by semana_liberada")
                    row = cursor.fetchall()
                    for r in row:
                        lista = listSemana()
                        lista.idsemana = r[0]
                        lista.ano = int(str(r[0])[0:4])
                        lista.semana = int(str(r[0])[4:6])
                        lista.link = "http://tupper-tools.herokuapp.com/api/liberadas/"+str(r[0])
                        try:
                            lista.save()
                        except expression as identifier:
                            pass
                        
        else:
            print("nao é numero")
    print("nao foi encontradas",count,"caixas")
