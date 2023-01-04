from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Request, Response, status
from .models import Report
from .permissions import IsUserReport
# Create your views here.
class ReportUserView(APIView):     
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserReport]
    
    def get(self, request: Request) -> Response:
        reports = Report.objects.all()

        serializer = ReportSerializer(reports, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)