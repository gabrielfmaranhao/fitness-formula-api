from django.urls import path
from .views import RatingView

urlpatterns = [
    path("ratings/user/<str:trainer_id>/", RatingView.as_view()),
]