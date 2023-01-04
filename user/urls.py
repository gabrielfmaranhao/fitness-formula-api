from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegisterView, UserSelfView, TrainerView, SingleTrainerView

urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("login/refresh/", TokenRefreshView.as_view()),
    path("users/self/", UserSelfView.as_view()),
    path("users/trainers/", TrainerView.as_view()),
    path("users/trainers/<int:pk>", SingleTrainerView.as_view()),
]
