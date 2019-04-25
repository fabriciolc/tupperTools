from django import forms
from .models import Ocorrencia
from home.models import Consultora
class OccurrenceForm(forms.ModelForm):
    garantia = forms.BooleanField(required=False)

    class Meta:
        model = Ocorrencia
        fields = ['consultora','codigo_produto','numero_nota','ocorrencia','observacao','nota','status','garantia']
      