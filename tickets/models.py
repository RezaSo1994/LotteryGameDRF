from django.db import models


class BuyTickets(models.Model):
    tickets = models.IntegerField()
    discunt = models.FloatField()

    def __str__(self) -> str:
        return 'Ticket :' + str(self.tickets)
