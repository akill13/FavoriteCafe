from django.db import models

# Create your models here.
class Cafe(models.Model):
    #Image
    image = models.ImageField(upload_to='images/')
    #Summary
    summary = models.CharField(max_length=200)
