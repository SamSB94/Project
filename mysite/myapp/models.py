from django.db import models


# Create your models here.

class Feedback(models.Model):
    email = models.EmailField()
    amount = models.FloatField()
    message = models.TextField()

    def __str__(self):
        return self.email


class Employees(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
