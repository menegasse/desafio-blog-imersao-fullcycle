from base.models import BaseTimestampedModel, BaseModel
from django.db import models


class Post(BaseModel, BaseTimestampedModel):
    title = models.CharField(max_length=100, unique=True, verbose_name='Título')
    content = models.TextField(verbose_name='')
    tags = models.ManyToManyField('Tag', verbose_name='Tags', related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nome')
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name