from django.db import models

# Create your models here.

class mainbd(models.Model):
    name=models.CharField(max_length=128)
    text=models.TextField()

    def __str__(self):
        return self.name