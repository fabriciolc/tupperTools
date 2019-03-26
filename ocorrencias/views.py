from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ocorrencia
from .forms import OccurrenceForm
# Create your views here.
@login_required
def ocorrencias_show(request):
    ocorrencias = Ocorrencia.objects.all()
    context = {}
    return render(request, "show_occurrence.html" , {'ocorrencias' : ocorrencias})

@login_required
def ocorrencias_new(request):
    form = OccurrenceForm(request.POST, request.FILES,None)
    if form.is_valid():
        form.save()
        return redirect('ocorrencias_show')
    return render(request, "form_occurrence.html",{'form' : form})

@login_required
def ocorrencias_edit(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=id)
    form = OccurrenceForm(request.POST or None, request.FILES or None, instance=ocorrencia)
    if form.is_valid():
        form.save()
        return redirect('ocorrencias_show')
    return render(request, 'form_occurrence.html',{'form': form})

@login_required
def ocorrencias_delete(request,id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=id)

    if request.method == 'POST':
        ocorrencia.delete()
        return redirect('ocorrencias_show')
    
    return 