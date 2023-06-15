from django.db import models

# Create your models here.

class Post(models.Model):

    choice = [(1, 'General'), (2, 'Music'), (3, 'Series/Movies'), (4, 'Sports')]


    autor = models.CharField(max_length=30)

    data = models.DateField(auto_now_add=True)

    typeOfChoice = models.IntegerField(choices = choice, default=1) 

    titulo = models.CharField(max_length=30)

    descricao = models.TextField(max_length=5000)

    link = models.URLField(blank=True, null=True)

    
    like = models.IntegerField(default=0)

    deslike = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo[:20]