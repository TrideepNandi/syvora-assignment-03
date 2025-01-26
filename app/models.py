from django.db import models

# Create your models here.
class GeeksModel (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)