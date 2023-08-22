from django.db import models

# Create your models here.
class Job(models.Model):
    pdate = models.DateField()
    location = models.CharField(max_length=100);
    offeredsalary = models.IntegerField();
    qualification = models.CharField(max_length=100);

class Book(models.Model):
    bno = models.IntegerField();
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50);
    publishdate = models.DateField();

class Customer(models.Model):
    name = models.CharField(max_length=100);
    accno = models.IntegerField();
    mailid = models.EmailField();
    phoneno = models.IntegerField();
    age = models.IntegerField();
