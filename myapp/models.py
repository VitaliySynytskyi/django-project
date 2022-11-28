from django.db import models

# Create your models here

class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    number= models.CharField(max_length=50)
    action= models.CharField(max_length=200)
    class Meta:
      db_table = "loggs"

class Logs1(models.Model):
    id = models.AutoField(primary_key=True)
    when= models.TimeField(max_length=50)
    name= models.CharField(max_length=50)
    number= models.CharField(max_length=50)
    action= models.CharField(max_length=200)
    class Meta:
      managed = False
      db_table = 'loggs'


class Cabinets(models.Model):
    id = models.AutoField(primary_key=True)
    number= models.CharField(max_length=50)
    name_teacher = models.CharField(max_length=50)
    class Meta:
      db_table = "cabinets"

