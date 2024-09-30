from .models import TodoDB
from django.shortcuts import render

from .serializer import TodoSerializer
from rest_framework import viewsets


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    queryset=TodoDB.objects.all()
    serializer_class=TodoSerializer

