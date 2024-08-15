from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TravelTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    
    BOOK_HOTEL_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('N/A', 'N/A'),
    ]
    book_hotel = models.CharField(
        max_length=3,
        choices=BOOK_HOTEL_CHOICES,
        default='N/A'
    )
    
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default='Not Started'
    )

    def __str__(self):
        return f"{self.destination} - {self.status}"