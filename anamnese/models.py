from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    senha = models.CharField(max_length=30)


class Anamnese(models.Model):
    fk_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    alergias = models.JSONField(default=list)  #Aceita tanto listas [] como dicionários
    estilo_alimentar = models.CharField(max_length=30)
    alimentos_bons = models.JSONField(default=list)
    alimentos_ruins = models.JSONField(default=list)
    comobirdades = models.JSONField(default=list)


class NotasFiscais(models.Model):
    chave_acesso = models.IntegerField(primary_key=True)
    fk_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
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
