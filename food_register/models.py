from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Usuarios(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'password']


class NotasFiscais(models.Model):
    chave_acesso = models.IntegerField(primary_key=True)
    fk_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(null=False)
    valor_total = models.FloatField()
    cnpj = models.IntegerField()
    metodo_pag = models.CharField(max_length=20)


class Categorias(models.Model):
    categoria = models.CharField(max_length=50, blank=False)


class ProdutosNotasFiscais(models.Model):
    nota_fk = models.ForeignKey(NotasFiscais, on_delete=models.CASCADE)
    un = models.FloatField(blank=False)
    valor_unitario = models.FloatField(blank=False)
    valor_total = models.FloatField(blank=False)
    nome = models.CharField(max_length=100, blank=False)
    marca = models.CharField(max_length=50, blank=False)
    categoria_fk = models.ForeignKey(Categorias, on_delete=models.CASCADE)