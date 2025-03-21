from rest_framework import  generics
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView
from car.models import Car, Category
from car.serializers import CarSerializer, CategorySerializer


class CarApi(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarCreateView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarByIdApiView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateApiView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDeleteApiView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CategoryListCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer