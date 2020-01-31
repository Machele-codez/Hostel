from django.db import models
from django.core import validators
from django.urls import reverse

# Create your models here.
class Room(models.Model):
    floor = models.CharField(max_length = 256)
    capacity = models.PositiveIntegerField(validators = [validators.MaxValueValidator(4,'Must not exceed 4 members')])

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("hostel:room_in_detail", kwargs={"pk": self.pk})
    


class Tenant(models.Model):
    name = models.CharField(max_length = 100)
    level = models.PositiveIntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name = 'tenants')
    # * student_id

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse("hostel:room_in_detail", kwargs={"pk": self.room.pk})
