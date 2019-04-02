from django.urls import path
from .views import form_liberadas
urlpatterns = [
    path('', form_liberadas, name="form_liberadas"),
]