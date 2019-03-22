from django.urls import path
from .views import ocorrencias_show,ocorrencias_new,ocorrencias_edit,ocorrencias_delete
urlpatterns = [
    path('show/', ocorrencias_show, name="ocorrencias_show"),
    path('new/', ocorrencias_new, name="ocorrencias_new"),
    path('edit/<int:id>', ocorrencias_edit, name="ocorrencias_edit"),
    path('delete/<int:id>', ocorrencias_delete, name="ocorrencias_delete"),
]