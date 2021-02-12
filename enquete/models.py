from django.db import models

class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    # texto_ref = models.URLField()
    data_pub = models.DateTimeField('data publicacao')

    def __str__(self):
        return self.texto


class Opcao(models.Model):
    perguta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_opc = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_opc