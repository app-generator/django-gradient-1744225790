# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    sobrenome = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Produto(models.Model):

    #__Produto_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    codigo_sistema = models.TextField(max_length=255, null=True, blank=True)

    #__Produto_FIELDS__END

    class Meta:
        verbose_name        = _("Produto")
        verbose_name_plural = _("Produto")


class Cliente(models.Model):

    #__Cliente_FIELDS__
    data_nascimento = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Cliente_FIELDS__END

    class Meta:
        verbose_name        = _("Cliente")
        verbose_name_plural = _("Cliente")


class Pedido(models.Model):

    #__Pedido_FIELDS__
    numero_pedido = models.IntegerField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    #__Pedido_FIELDS__END

    class Meta:
        verbose_name        = _("Pedido")
        verbose_name_plural = _("Pedido")



#__MODELS__END
