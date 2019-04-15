from django.forms import ModelForm
from .models import Ocorrencia
from home.models import Consultora
class OccurrenceForm(ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['consultora','codigo_produto','numero_nota','ocorrencia','observacao','nota','status']
      