from django.urls import path

from app import views

urlpatterns = [
    path("car/create/", views.CarCreateApi.as_view()),

]