from django.db import models
from django.contrib.auth.models import User


# Choices for booking hotel status
BOOK_HOTEL_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('N/A', 'N/A'),
]

# Choices for task status
STATUS_CHOICES = [
    ('Not Started', 'Not Started'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
]

# Choices for transportation method
TRANSPORTATION_CHOICES = [
    ('Flight', 'Flight'),
    ('Train', 'Train'),
    ('Bus', 'Bus'),
    ('Own Vehicle', 'Own Vehicle'),
    ('Bicycle', 'Bicycle'),
    ('Boat', 'Boat'),
    ('Other', 'Other'),
]

# Create your models here.
class TravelTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    book_hotel = models.CharField(
        max_length=3,
        choices=BOOK_HOTEL_CHOICES,
        default='N/A'
    )

    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default='Not Started'
    )

    transportation = models.CharField(
        max_length=12,
        choices=TRANSPORTATION_CHOICES,
        default='Flight'
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.destination} ({self.start_date} - {self.end_date})"