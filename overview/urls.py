from django.urls import path
from .views import OverviewStaffView, OverviewDeleteView, OverviewStudentView

urlpatterns = [
    path('overview/user/<str:student_id>', OverviewStaffView.as_view()),
    path('overview/user', OverviewStudentView.as_view()),
    path('overview/<str:overview_id>', OverviewDeleteView.as_view())
]