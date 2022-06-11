from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    idUser = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.username