from django.db import models
from django.conf import settings
from django.utils import timezone
import os
# Create your models here.





class Welcome(models.Model):
    text = models.TextField()

class Description(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    icon_image = models.ImageField(db_column='imagefile', upload_to='media/', null=True, blank=True, help_text="Load an image.")
    
