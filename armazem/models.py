from django.db import models


class Alimentos(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.CharField(unique=True, max_length=15)
    quantidade = models.IntegerField()
    fk_id_usuario = models.ForeignKey('Usuarios', models.CASCADE, db_column='fk_id_usuario')


class UsuarioPreferencias(models.Model):
    restricoes = models.CharField(max_length=100)
    preferidos = models.CharField(max_length=100)
    rejeitados = models.CharField(max_length=100)
    fk_id_usuario = models.ForeignKey('Usuarios', models.CASCADE, db_column='fk_id_usuario')


class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.CharField(unique=True, max_length=100)
    senha = models.CharField(max_length=30)