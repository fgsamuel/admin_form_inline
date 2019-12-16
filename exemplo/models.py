from django.db import models

# Create your models here.


class Pai(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome


class FilhoA(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    pai = models.ForeignKey(Pai, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "filhos A"

    def __str__(self):
        return self.nome


class FilhoB(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    pai = models.ForeignKey(Pai, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "filhos B"

    def __str__(self):
        return self.nome
