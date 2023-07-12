from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return HttpResponse("<h1>Hello Bro</h1>")


class RoomView(generics.ListAPIView): #using CreateAPIView for post api
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
