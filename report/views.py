from rest_framework.generics import (ListAPIView)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Report
from user.models import User
from .permissions import IsUserReport, IsTrainerReport
from .serializer import ReportSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
import ipdb
from rest_framework import generics, exceptions


class ReportUserView(APIView):     
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTrainerReport]
    
    def get(self, request: Request) -> Response:
        reports = Report.objects.all()

        self.check_object_permissions(request, reports)
        serializer = ReportSerializer(reports, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

class OneReportUserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserReport, IsTrainerReport]

    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.filter(
            report_student=self.kwargs["students_id"], report_trainer=self.request.user
        )

    def perform_create(self, serializer):
        student_id = self.kwargs["student_id"]
        
        student_obj = get_object_or_404(User, id=student_id)
        
        student_report = Report.objects.filter(student_id = student_obj)
        # student_report_exists = student_report.exists()
       
        ipdb.set_trace()
    
        serializer.save(report=student_report.first())
    
    # def get(self, request: Request, id) -> Response:
    #     report = Report.objects.get(id = id)
    #     self.check_object_permissions(request, report)
    #     serializer = ReportSerializer(report)
        
    #     if self.authentication_classes == False:
    #                     return Response(
    #                     {"detail": "Authentication credentials were not provided."}, status.HTTP_401_UNAUTHORIZED
    #                     )
        
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def post(self, request: Request, student_id) -> Response:
    #     student_obj = get_object_or_404(User, id=student_id)
    #     user_report = Report.objects.filter(student_id = student_obj)
    #     ipdb.set_trace()
    #     self.check_object_permissions(request, user_report)
    #     serializer = ReportSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(report = user_report)
        
    #     return Response(serializer.data, status.HTTP_201_CREATED)


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