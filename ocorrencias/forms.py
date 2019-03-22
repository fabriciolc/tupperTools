from django.forms import ModelForm
from .models import Ocorrencia
class OccurrenceForm(ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['codigo_consultora','codigo_produto','numero_nota','ocorrencia','observacao','nota','status']
        


