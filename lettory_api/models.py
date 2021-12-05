from django.db import models
from .models import generateToken


class Tickets(models.Model):
    key = models.CharField(max_length=255)
    number = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return str(self.number)


class UserData(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    total_mony = models.IntegerField()
    tickets = models.ForeignKey(Tickets, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.username


class TotalData(models.Model):
    prize_pot = models.IntegerField()
    drow_time = models.DateField()
    round = models.IntegerField()
    drawn_last_time = models.TimeField()
    winning_number = models.DateField()

    def __str__(self) -> str:
        return str(self.round)


class generateToken(models.Model):
    arr = models.JSONField(generateToken())
