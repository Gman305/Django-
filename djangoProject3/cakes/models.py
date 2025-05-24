from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Cake(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='cakes/', null=True, blank=True)
    baker=models.ForeignKey('Baker', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}, {self.price}"

class Baker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20)
    email = models.EmailField()
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.name}, {self.surname}, {self.phone_number}"