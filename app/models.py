import django
from django.conf import settings
from django.db import models


class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=200,default='My Wallet')
    bitcoin = models.DecimalField(decimal_places=20,max_digits=100,default=0)
    etherium = models.DecimalField(decimal_places=20,max_digits=100,default=0)
    litecoin = models.DecimalField(decimal_places=20,max_digits=100,default=0)

class Roles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    role = models.CharField(max_length=200,default='user')
