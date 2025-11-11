from django.urls import path
from . import views

urlpatterns = [
    path("", views.closest_matches, name="home"),
]
