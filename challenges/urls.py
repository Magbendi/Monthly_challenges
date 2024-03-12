from django.urls import path

from . import views

urlpatterns = [
path("", views.index),
path("<int:m>", views.monthly_challenge_by_number),
path("<str:m>", views.monthly_challenges, name= "month-challenge"),
]