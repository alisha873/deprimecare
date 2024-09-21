from django.db import models

class Counselor(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.URLField()  # Store image URLs
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Create your models here.
