from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

# class DocListItem(models.Model):
#     user = models.CharField(max_length=100)
    # content = models.TextField()
    # dateof = models.DateField()

SERVICE_CHOICES = (
    ("Doctor care", "Doctor care"),
    ("Nursing care", "Nursing care"),
    )

TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

class Appointment(models.Model):
    user = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, default="Doctor care")
    day = models.CharField(max_length=50)
    time = models.CharField(max_length=10, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.user_name} | day: {self.day} | time: {self.time}"