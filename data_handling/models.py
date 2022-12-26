from django.db import models

# Create your models here.
from djongo import models


class myrecord(models.Model):
    #ID=models.BigIntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}({self.id})'

