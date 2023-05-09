from django.db import models

# Create your models here.
class libro (models.Model):
    Nombre=models.CharField(max_length=50)
    Autor=models.CharField(max_length=50)
    Editorial=models.CharField(max_length=50)
    stock=models.PositiveIntegerField()
    