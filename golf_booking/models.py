"""
Importing User to use as foreign key in booking model
phone_number_field used to ensure correct country code
"""
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

NUMBER_OF_HOLES = ((9, "9"), (18, "18"))
NUMBER_OF_PLAYERS = ((1, "1"), (2, "2"), (3, "3"), (4, "4"))
TEE_TIMES = (
    ("08:00", "08:00"), ("08:30", "08:30"), ("09:00", "09:00"),
    ("09:30", "09:30"), ("10:00", "10:00"), ("10:30", "10:30"),
    ("11:00", "11:00"), ("11:30", "11:30"), ("12:00", "12:00"),
    ("12:30", "12:30"), ("13:00", "13:00"), ("13:30", "13:30"),
    ("14:00", "14:00"), ("14:30", "14:30"), ("15:00", "15:00"),
    ("15:30", "15:30"), ("16:00", "16:00"), ("16:30", "16:30"),
    ("17:00", "17:00")
    )
BOOKING_STATUS = ((0, "Pending"), (1, "Confirmed"))


class Booking(models.Model):
    """
    Model holds each booking requested
    Linked with logged in user as foreign key
    Booking status used to display bookings to
    user only if 'Confirmed'.
    """
    booking_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    number_of_holes = models.IntegerField(choices=NUMBER_OF_HOLES, default=0)
    number_of_players = models.IntegerField(
        choices=NUMBER_OF_PLAYERS, default=0
        )
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    club_hire = models.BooleanField(null=False, blank=False, default=False)
    play_date = models.DateField(null=True)
    play_time = models.CharField(
        choices=TEE_TIMES, default=False, max_length=10
        )
    extra_requests = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """To set profile orders based on 'created_on' date"""
        ordering = ['-created_on']

    def __str__(self):
        return str(self.last_name)
