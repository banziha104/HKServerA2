from django.db import models
from section.models import Section
from contentType.models import ContentType
# Create your models here.

class HKData(models.Model):
    title = models.CharField(max_length=200,db_index=True)
    description = models.TextField(default="")
    section = models.ForeignKey(Section, related_name= 'data_section')
    type = models.ForeignKey(ContentType, related_name= 'type_string', null=True)
    lat = models.CharField(null=False,max_length=200)
    lon = models.CharField(null=False,max_length=200)
    image = models.ImageField(upload_to='HKmodel/%Y/&m/%d', default='NoImage.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.title)



