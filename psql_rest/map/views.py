from django.shortcuts import render

# Create your views here.
import django_filters
from rest_framework import viewsets, filters
from .models import japan_ver81
from .serializer import japan_ver81_Serializer

class japan_ver81_VewSet(viewsets.ModelViewSet):
	queryset = japan_ver81.objects.all()
	serializer_class = japan_ver81_Serializer
