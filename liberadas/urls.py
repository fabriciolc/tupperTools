from django.urls import path
from .views import form_caixas_fabrica,form_liberadas
urlpatterns = [
    path('', form_caixas_fabrica, name="form_caixas_fabrica"),
    path('lb/', form_liberadas, name="form_liberadas"),
]