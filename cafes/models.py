from django.db import models

# Create your models here.
class Cafe(models.Model):
    #Image
    image = models.ImageField(upload_to='images/')
    #Summary
    summary = models.CharField(max_length=200)
    #Name
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.summary
