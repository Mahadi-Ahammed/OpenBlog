from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Destination(models.Model):
    name= models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics' )
    desc= models.CharField(max_length=300)
    price= models.IntegerField()
    offer=models.BooleanField(default=False)


