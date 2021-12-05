from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from lettory_api.models import UserData, TotalData
from lettory_api.serializer import UserDataSerializer, TotalDataSerializer


class UserDataList(ListCreateAPIView):
    queryset = UserData.objects.all()
    # serializer_class = ProductSerializer
    serializer_class = UserDataSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TotalDataList(ListCreateAPIView):
    queryset = TotalData.objects.all()
    serializer_class = TotalDataSerializer

    def get_serializer_context(self):
        return {'request': self.request}
