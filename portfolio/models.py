from django.db import models
from django.db.models.fields import CharField, URLField
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = CloudinaryField(upload_to='image')
    url = URLField(blank=True)
