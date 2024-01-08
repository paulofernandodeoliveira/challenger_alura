from django.db import models

class Video(models.Model):
    ID = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length = 500)
    Descricao = models.CharField(max_length = 500)
    link = models.CharField(max_length = 500)