from django.urls import path
from . import views


urlpatterns = [
    path("sheets/new/user/<str:id>/", views.SheetView.as_view()),
    path("sheets/user/<str:student_id>/", views.SheetDetailView.as_view()),
    path("sheets/user/", views.SheetSelfView.as_view()),
]
