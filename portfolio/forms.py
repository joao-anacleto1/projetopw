from django.forms import ModelForm

from .models import Post


class Postform(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['data','like','deslike']

        labels = {
            'autor': 'Author',
            'titulo': 'Title',
            'descricao': 'Post',
            'link' : 'Link',
        }