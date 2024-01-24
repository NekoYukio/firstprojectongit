from django.db import models

# Create your models here.
class AboutDB(models.Model):
    name=models.CharField(max_length=128)
    cost=models.IntegerField()
    hours=models.IntegerField()

    def __str__(self):
        return self.name