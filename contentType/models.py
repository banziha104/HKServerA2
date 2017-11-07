from django.db import models

# Create your models here.

class ContentType(models.Model):
    types = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.types)