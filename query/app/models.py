from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    marks = models.IntegerField()
    pass_date = models.DateField()

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    empnum = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=50)
    salary = models.IntegerField()
    join_date = models.DateField()

    def __str__(self):
        return self.name
