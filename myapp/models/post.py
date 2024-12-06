from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor_id = models.IntegerField()  # Use ForeignKey se tiver um modelo Autor

    def __str__(self):
        return self.titulo