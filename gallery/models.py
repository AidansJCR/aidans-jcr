from django.db import models

# Create your models here.

class AlbumPage(Page):
    description = models.TextField()
    
