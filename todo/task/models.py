from django.db import models

# Create your models here.
class todo(models.Model):
    slno=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=200)
    date=models.DateField()


class todotask(models.Model):
    slno=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    due_date=models.DateField()