from django.db import models

# Create your models here.


class user(models.Model):
    fullname = models.TextField()
    email = models.TextField()
    phone_number = models.TextField()
