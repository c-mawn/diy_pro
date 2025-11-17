from django.urls import path
from . import views

urlpatterns = [
    path("/closest_matches", views.closest_matches, name="closest_matches"),
]
