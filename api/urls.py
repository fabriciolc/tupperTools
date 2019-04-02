from django.urls import path
from .views import api_liberadas, api_listLiberada


urlpatterns = [
    path('liberadas/<int:semana>', api_liberadas.as_view() , name="api_liberadas"),
    path('liberadas/list', api_listLiberada.as_view() , name="api_listLiberada")
]