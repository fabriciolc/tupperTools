from django import forms
from .models import Ocorrencia
from home.models import Consultora
class OccurrenceForm(forms.ModelForm):

    class Meta:
        model = Ocorrencia
        fields = ['consultora','codigo_produto','numero_nota','observacao','nota','status','garantia','ocorrencia','nomeProduto','semanaNota']
      