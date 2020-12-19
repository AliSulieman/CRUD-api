from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class user(models.Model):
    fullname = models.TextField(validators=[MinLengthValidator(5)])
    email = models.TextField(validators=[MinLengthValidator(11)])
    password = models.TextField(validators=[MinLengthValidator(6)])
