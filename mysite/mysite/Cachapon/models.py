from django.db import models

# Create your models here.
class ImageTest(models.Model):
    image1 = models.ImageField(upload_to='Cachapon/images/')
