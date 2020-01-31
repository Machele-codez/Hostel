from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length = 40)
    lastname = models.CharField(max_length = 40)
    username = models.CharField(max_length = 40, unique = True)
    email = models.EmailField(max_length = 100, primary_key = True,)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.username