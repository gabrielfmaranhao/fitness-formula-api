from django.urls import path
from .views import RatingView

urlpatterns = [
    path("ratings/trainer/<str:trainer_id>/", RatingView.as_view()),
]