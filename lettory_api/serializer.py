from rest_framework import serializers
from lettory_api.models import UserData, Tickets, TotalData


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'


class TotalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalData
        fields = '__all__'
