from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from tickets.models import BuyTickets
from tickets.serializer import BuyTicketsSerializer


class BuyTicketsList(ListCreateAPIView):
    queryset = BuyTickets.objects.all()
    # serializer_class = ProductSerializer
    serializer_class = BuyTicketsSerializer

    def get_serializer_context(self):
        return {'request': self.request}
