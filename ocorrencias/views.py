from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ocorrencia
from .forms import OccurrenceForm
# Create your views here.
@login_required
def ocorrencias_show(request):
    ocorrencias = Ocorrencia.objects.all()
    context = {
        'ocorrencias':ocorrencias,
    }
    return render(request, "show_occurrence.html" ,{'ocorrencias' : ocorrencias})

@login_required
def ocorrencias_new(request):
    form = OccurrenceForm()
    context = {
        'form' : form,
        'titulo': 'Nova Ocorrencia',
    }
    if request.method == "POST":
        form = OccurrenceForm(request.POST, request.FILES,None)
        files = request.FILES.getlist('nota')
        if form.is_valid():
            ocorrencia = form.save(commit=False)
            if(request.POST.get('typeOccurrence') == 'Garantia'):
                ocorrencia.garantia = True
            ocorrencia.save()
            return redirect("ocorrencias_show")
        else:
            print(form.errors)
            return redirect("ocorrencias_show")
    else:
        form = OccurrenceForm()
        context = {
            'form' : form,
            'titulo': 'Nova Ocorrencia',
        }
        return render(request, "form_occurrence.html",context)
    return render(request, "form_occurrence.html",context)



@login_required
def ocorrencias_edit(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=id)
    form = OccurrenceForm(request.POST or None, request.FILES or None, instance=ocorrencia)
    context = {
        'form' : form,
        'titulo': 'Editar Ocorrencia',
        'garantia' : ocorrencia.garantia
    }
    if form.is_valid():
        ocorrencia = form.save(commit=False)
        if(request.POST.get('typeOccurrence') == 'Garantia'):
            ocorrencia.garantia = True
        ocorrencia.save()
        return redirect('ocorrencias_show')
    return render(request, 'form_occurrence.html',context)

@login_required
def ocorrencias_delete(request,id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=id)

    if request.method == 'POST':
        ocorrencia.delete()
        return redirect('ocorrencias_show')
    
    return 