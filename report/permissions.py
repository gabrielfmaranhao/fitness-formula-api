from rest_framework import permissions
from user.models import User

class IsTrainerReport(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:
        return request.user.is_staff and request.user.id

class IsTrainer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff == True