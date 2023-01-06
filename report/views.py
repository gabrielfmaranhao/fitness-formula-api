from django.shortcuts import render
from rest_framework.generics import (RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, RetrieveAPIView,)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from .models import Report
from .permissions import IsUserReport, IsTrainerReport
from .serializer import ReportSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class ReportUserView(ListAPIView):     
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserReport]
    
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

class OneReportUserView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserReport]

    serializer_class = ReportSerializer
    queryset = Report.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        report = get_object_or_404(queryset, id=self.request.report.id)

        self.check_object_permissions(self.request, report)

        return report


class ReportTrainerView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTrainerReport]
    
    serializer_class = ReportSerializer
    queryset = Report.objects.all()