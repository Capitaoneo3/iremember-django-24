from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return self.titulo
