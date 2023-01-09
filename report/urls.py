from django.urls import path
from . import views


urlpatterns = [
    path("reports/user/", views.ReportUserView.as_view()),
    path("reports/user/<str:student_id>/", views.OneReportUserView.as_view()),
    path("reports/trainer/", views.ReportTrainerView.as_view()),
    path("reports/<str:id>/", views.OneReportView.as_view()),
]
