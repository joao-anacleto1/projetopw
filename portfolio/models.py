from django.db import models

# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=30)
    data = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField(max_length=5000)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo[:20]