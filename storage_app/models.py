from django.db import models

# Create your models here.


class Image(models.Model):    
    
    image_url = models.URLField(blank=True)
    download_url = models.URLField(blank=True)