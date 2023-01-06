from rest_framework import permissions
from user.models import User

import ipdb

class IsUserReport(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:  
            return request.user == user

class IsTrainerReport(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:
        return request.user.is_staff and request.user.id

