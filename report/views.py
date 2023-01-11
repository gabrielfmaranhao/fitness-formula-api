from rest_framework.generics import (ListAPIView)
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Report
from user.models import User
from .permissions import IsTrainer
from .serializer import ReportSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ReportUserView(ListAPIView):     
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.filter(student_id=self.request.user)
   
class OneReportUserView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTrainer]

    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.filter(student_id=self.kwargs["student_id"])

    def perform_create(self, serializer):
        student_id = self.kwargs["student_id"]
        
        student_obj = get_object_or_404(User, id=student_id)
    
        serializer.save(student=student_obj, trainer=self.request.user)

class ReportTrainerView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTrainer]
    
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

class OneReportView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTrainer]

    def get(self, request: Request, id) -> Response:
        report = get_object_or_404(Report, id=id)

        self.check_object_permissions(request, report)
        serializer = ReportSerializer(report)
        
        if self.authentication_classes == False:
                        return Response(
                        {"detail": "Authentication credentials were not provided."}, status.HTTP_401_UNAUTHORIZED
                        )
        if report == False:
            return Response({
                 {"detail": "Report did not exists."}, status.HTTP_404_NOT_FOUND
            })
        
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, id) -> Response:
        report = get_object_or_404(Report, id=id)        

        serializer = ReportSerializer(report, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, id) -> Response:
            report = get_object_or_404(Report, id=id)        
            report.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)