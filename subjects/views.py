from django.shortcuts import render
from rest_framework import generics 
from .models import Subject
from .serializers import SubjectSerializer

class SubjectListAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer