from rest_framework.views import APIView, Request, Response, status
from .serializers import OverviewSerializer
from .models import Overview
from user.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAuthenticated, IsStaff, IsStaffOwner


class OverviewStaffView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStaff]

    def get(self, request: Request, student_id: str) -> Response:
        student = get_object_or_404(User, id=student_id)

        overviews = Overview.objects.filter(student=student)

        serializer = OverviewSerializer(overviews, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, student_id: str) -> Response:
        student = get_object_or_404(User, id=student_id)

        serializer = OverviewSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(student=student, created_by=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OverviewDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStaff, IsStaffOwner]
    
    def delete(self, request: Request, overview_id: str) -> Response:
        overview = get_object_or_404(Overview, id=overview_id)

        self.check_object_permissions(request, overview)

        overview.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class OverviewStudentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        overviews = Overview.objects.filter(student=request.user)

        serializer = OverviewSerializer(overviews, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
