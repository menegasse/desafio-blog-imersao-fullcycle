
from django.db import models
from base.manager import BaseManagerUsingDatabase

class BaseModel(models.Model):
    objects: BaseManagerUsingDatabase = BaseManagerUsingDatabase()
    id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    class Meta: 
        abstract = True
    

class BaseTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True