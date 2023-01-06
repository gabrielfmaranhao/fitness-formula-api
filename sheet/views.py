from django.shortcuts import get_object_or_404
from rest_framework import generics, exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from user.models import User
from workout.serializers import WorkoutSerializer
from workout.models import Workout
from .permissions import IsSheetOwner, IsTrainer
from .serializers import SheetSerializer
from .models import Sheet
import ipdb

# Create your views here.
class SheetView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsTrainer]

    serializer_class = SheetSerializer

    def perform_create(self, serializer):
        student_id = self.kwargs["id"]
        student_obj = get_object_or_404(User, pk=student_id)

        student_sheet = Sheet.objects.filter(student_id=student_obj).exists()

        if student_sheet:
            Sheet.objects.get(student_id=student_obj).delete()

        serializer.save(trainer=self.request.user, student=student_obj)


class SheetSelfView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = SheetSerializer
    queryset = Sheet.objects.all()

    def get_object(self):
        return get_object_or_404(self.queryset, student_id=self.request.user)


class SheetDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsTrainer]

    serializer_class = SheetSerializer
    lookup_field = "student_id"

    def get_queryset(self):
        return Sheet.objects.filter(trainer_id=self.request.user)

    def perform_update(self, serializer):
        student_id = self.kwargs["student_id"]
        student_obj = get_object_or_404(User, pk=student_id)

        serializer.save(trainer=self.request.user, student=student_obj)


class WorkoutView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsTrainer, IsSheetOwner]

    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.filter(
            sheet__student=self.kwargs["student_id"], sheet__trainer=self.request.user
        )

    def perform_create(self, serializer):
        student_id = self.kwargs["student_id"]
        student_obj = get_object_or_404(User, pk=student_id)

        student_sheet = Sheet.objects.filter(student_id=student_obj)
        student_sheet_exists = student_sheet.exists()

        self.check_object_permissions(self.request, student_sheet.first())

        if student_sheet_exists is False:
            raise exceptions.NotFound("Training sheet not found.")

        serializer.save(sheet=student_sheet.first())


class WorkoutSelfView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.filter(sheet__student=self.request.user)


class WorkoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsTrainer]

    serializer_class = WorkoutSerializer
    lookup_url_kwarg = "workout_id"

    def get_queryset(self):
        return Workout.objects.filter(sheet__trainer=self.request.user)
