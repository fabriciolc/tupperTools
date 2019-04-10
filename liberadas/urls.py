from django.urls import path
from .views import form_liberadas,show_liberadas
urlpatterns = [
    path('', form_liberadas, name="form_liberadas"),
    path('show/', show_liberadas, name="show_liberadas"),
]