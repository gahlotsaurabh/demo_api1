from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.renderers import TemplateHTMLRenderer
from api_demo.models import Category, Products
# from api_demo.serializers import ProductSerializer, CategorySerializer
from rest_framework import generics,filters,viewsets
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import ProductSerializer, CategorySerializer

class CategoryView(generics.ListAPIView):
	serializer_class = CategorySerializer
	queryset = Category.objects.all()

class ProductView(generics.ListAPIView):
	serializer_class = ProductSerializer
	queryset = Products.objects.all()
