from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
        
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class listSemana(models.Model):
        idsemana = models.IntegerField(primary_key=True)
        semana = models.IntegerField()
        ano = models.IntegerField()
        link = models.TextField()

