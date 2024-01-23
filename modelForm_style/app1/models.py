from django.db import models

class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=20)
    dob = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    c_pass = models.CharField(max_length=20)
    agree = models.BooleanField()

    def __str__(self):
        return f'{self.roll} {self.name} {self.dob} {self.email} {self.address} {self.gender} '
