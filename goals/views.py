from django.shortcuts import render
from rest_framework import generics
from .serializers import GoalSerializer 
from .models import Goal

class GoalListAPIView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class GoalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer