from email.mime import image

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pilot(models.Model):
    RANK_CHOICES = [
        ("J","Junior"),
        ("I","Intermediate"),
        ("S","Senior"),
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.IntegerField()
    total_hours = models.DecimalField(max_digits=5, decimal_places=2)
    rank = models.CharField(max_length=1, choices=RANK_CHOICES)

    def __str__(self):
        return f"{self.name}  {self.surname}"



class Balloon(models.Model):
    TYPE_CHOICES = [
        ("S","Small"),
        ("M","Medium"),
        ("L","Large"),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    manufacturer = models.CharField(max_length=100)
    max_passengers = models.IntegerField()

    def __str__(self):
        return f"{self.name}  {self.manufacturer}"


class Company(models.Model):
    name = models.CharField(max_length=100)
    founding_year = models.IntegerField()
    flies_out_of_europe = models.BooleanField()

    def __str__(self):
        return f"{self.name}  {self.founding_year}"

class AirLinePilot(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company}  {self.pilot}"

class Flight(models.Model):
    code=models.CharField(max_length=100, unique=True)
    landing_airport=models.CharField(max_length=100)
    take_off_airport=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=image.ImageField(upload_to='flight_photos',null=True, blank=True)
    balloon=models.ForeignKey(Balloon, on_delete=models.CASCADE)
    airline=models.ForeignKey(Company, on_delete=models.CASCADE)
    pilot=models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.take_off_airport}-{self.landing_airport}"