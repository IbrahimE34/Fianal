
# (CreateAPIView, RetrieveAPIView,
#  UpdateAPIView, DestroyAPIView, ListCreateAPIView)

from django.urls import path
from car import views

urlpatterns = [
    path("create/car/", views.CreateAPIView.as_view()),
    path("retrieve/car/", views.RetrieveAPIView.as_view()),
    path("update/car/", views.UpdateAPIView.as_view()),
    path("destroy/car/", views.DestroyAPIView.as_view()),
    path("list/car/", views.ListCreateAPIView.as_view()),

]
