from django.db import models
from django.core import validators
from django.urls import reverse

# Create your models here.
class Room(models.Model):
    number = models.PositiveIntegerField(primary_key = True)
    floor = models.CharField(max_length = 256)
    capacity = models.PositiveIntegerField(validators = [validators.MaxValueValidator(4,'Must not exceed 4 members')])

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse("hotel:room_in_detail", kwargs={"pk": self.pk})
    
class Tenant(models.Model):
    student_ID = models.CharField(max_length = 10, primary_key=True)
    name = models.CharField(max_length = 100)
    level = models.PositiveIntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name = 'tenants')
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse("hotel:room_in_detail", kwargs={"pk": self.room.pk})


    

