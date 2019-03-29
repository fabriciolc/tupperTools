from django.shortcuts import render
from home.models import Consultora
from .models import Caixa_fabrica,Liberada
from io import TextIOWrapper
from django.http import JsonResponse
import datetime
import os, csv

# Create your views here.
def is_number(s):
    try:
        float(s)
        if s == "":
            return False
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def form_caixas_fabrica(request):
    if request.method == "POST":
        uploaded_file = request.FILES['uploaded_file'].read() # get the uploaded file
        for a in uploaded_file.splitlines():
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
            except expression as identifier:
                pass
            
        return render(request, 'indexliberada.html')
    else:
        return render(request, 'indexliberada.html')

def form_liberadas(request):
    if request.method == "POST":
        csvfile = TextIOWrapper(request.FILES['uploaded_file'].file)
        reader = csv.reader(csvfile,delimiter=";")
        for row in reader:
            if is_number(row[3]):
                rota = int(row[0])
                semana = int(row[1])
                totalcaixa = row[2]
                codigo_consultora = int(row[3])
                nome_consultora = row[4]
                entregador = row[5][0:15]
                
                #print(codigo_consultora)

                caixa = Caixa_fabrica.objects.filter(consultora=codigo_consultora,semana=semana)

                print(caixa)
                if not caixa:
                    print("teste")
                else:
                    for cx in caixa:
                        print("Teste",cx)
                        liberada = Liberada()
                        liberada.consultora = cx.consultora
                        liberada.semana = cx.semana
                        liberada.rota = cx.rota
                        liberada.entregador = entregador
                        liberada.volume_atual = cx.volume_atual
                        liberada.volume_total = cx.volume_total
                        liberada.semana_liberada = int(datetime.datetime.now().strftime("%Y%V"))
                        liberada.caixa_fabrica = cx
                        liberada.save()
                    #liberada.caixa_fabrica = caixa.codigo_caixa
            else:
                print("nao é numero")

        data = list(Liberada.objects.values())
        return JsonResponse(data, safe=False)

    return render(request, 'indexliberada.html')

