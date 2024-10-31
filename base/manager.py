import os
from django.db import models

class BaseManagerUsingDatabase(models.Manager):
    def get_queryset(self):
        print(os.environ.get("USING_DATABASE", "default"))
        return (
            super()
            .get_queryset()
            .using(os.environ.get("USING_DATABASE", "default"))
        )