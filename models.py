from django.db import models

# Create your models here.

class Studentdetails(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    major = models.CharField(max_length=150)
    year = models.CharField(max_length=150)
    gpa = models.DecimalField(
                max_digits=3,
                decimal_places=2)
    
