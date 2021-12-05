from rest_framework import serializers
from tickets.models import BuyTickets


class BuyTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyTickets
        fields = '__all__'
