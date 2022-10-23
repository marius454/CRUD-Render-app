from email.policy import default
from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)



class Book(models.Model):
    author_name = models.CharField(max_length=50)
    book_name = models.CharField(max_length=100)
    price = models.FloatField()
    release_date = models.DateField(default="1970-01-01")
    availability = models.BooleanField(default=False)

