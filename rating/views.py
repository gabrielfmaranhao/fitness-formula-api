from django.shortcuts import render
from .permissions import IsStudent
from .serializers import RatingSerializer
from user.models import User

from rest_framework import generics, exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class RatingView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStudent]
    serializer_class = RatingSerializer

    def perform_create(self, serializer):

        trainer_id = self.kwargs["trainer_id"]
        trainer = get_object_or_404(User, id=trainer_id)
        if trainer.is_staff is False:
            raise exceptions.NotFound("Trainer not found")

        serializer.save(trainer=trainer, student=self.request.user)


    
    
        
