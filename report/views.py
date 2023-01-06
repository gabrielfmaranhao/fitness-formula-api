from rest_framework.generics import (ListAPIView, RetrieveAPIView)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Report
from .permissions import IsUserReport, IsTrainerReport
from .serializer import ReportSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status

# Create your views here.
class ReportUserView(APIView):     
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTrainerReport]
    
    def get(self, request: Request) -> Response:
        reports = Report.objects.all()

        self.check_object_permissions(request, reports)
        serializer = ReportSerializer(reports, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

class OneReportUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserReport, IsTrainerReport]

    def get(self, request: Request, id) -> Response:
        report = Report.objects.get(id = id)
        self.check_object_permissions(request, report)
        serializer = ReportSerializer(report)
        
        if self.authentication_classes == False:
                        return Response(
                        {"detail": "Authentication credentials were not provided."}, status.HTTP_401_UNAUTHORIZED
                        )
        
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request, user_id) -> Response:
        
        report_obj = Report.objects.get(user_id = user_id)

        self.check_object_permissions(request, report_obj)
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(report = report_obj)
        
        return Response(serializer.data, status.HTTP_201_CREATED)


class ReportTrainerView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTrainerReport]
    
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

class OneReportView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserReport, IsTrainerReport]

    def get(self, request: Request, id) -> Response:
        report = Report.objects.get(id = id)
        self.check_object_permissions(request, report)
        serializer = ReportSerializer(report)
        
        if self.authentication_classes == False:
                        return Response(
                        {"detail": "Authentication credentials were not provided."}, status.HTTP_401_UNAUTHORIZED
                        )
        
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, id) -> Response:
        report = get_object_or_404(Report, id=id)        

        serializer = ReportSerializer(report, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, id) -> Response:

            report = Report.objects.get(id = id)

            report.delete()

            return Response(204)