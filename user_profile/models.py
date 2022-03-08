from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

GENDER_STATUS = ((0, "I Prefer Not To Say"), (1, "Male"), (2, "Femail"))


class Profile(models.Model):
    """
    Class that hold each user's profile
    details. Onetoone relationship with
    logged in user
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    gender = models.IntegerField(choices=GENDER_STATUS, default=0)
    age = models.IntegerField(
        validators=[MinValueValidator(16), MaxValueValidator(100)])
    country = CountryField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """To set profile orders based on 'created_on' date"""
        ordering = ['-created_on']

    def __str__(self):
        return self.user.username
