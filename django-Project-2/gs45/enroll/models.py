from django.db import models

# Create your models here.

class User(models.Model):
    student_name = models.CharField(max_length=40)
    teacher_name = models.CharField(max_length=40)
    password = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100)