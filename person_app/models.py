# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# class CustomUser(AbstractUser):
#     pass

# Person entity fields
class Person(models.Model):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email_id = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

