from django.db import models
from django.contrib.auth.models import AbstractUser

class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

class Student(AbstractUser):
    student_name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    student_email = models.EmailField(unique=True)
    parent_email = models.EmailField()
    student_phone = models.CharField(max_length=11)
    parent_phone = models.CharField(max_length=11)
    student_CNIC = models.CharField(max_length=13)
    parent_CNIC = models.CharField(max_length=13)
    grades = [('preend','preend'),('ics_stat','ics_stat'),('ics_cs','ics_cs'),('premed','premed')]
    grade = models.CharField(max_length=10,choices=grades)
    subjects = models.ManyToManyField(Subject,null=False)

    
    def __str__(self):
        return self.username
    