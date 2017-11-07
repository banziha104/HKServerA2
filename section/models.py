from django.db import models

# Create your models here.

class Section(models.Model):
    section_name = models.CharField(null=False,max_length=200)
    lat = models.CharField(null=False,max_length=200)
    lon = models.CharField(null=False,max_length=200)

    def __str__(self):
        return str(self.section_name)