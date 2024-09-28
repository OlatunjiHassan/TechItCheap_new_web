from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    # if category == "webdesign":

    image = models.FileField(upload_to='project_images/', blank=True)
