from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Report
from ..user.models import User
class IsUserReport(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
            
        if request.user == user:
            return True
        if request.user != user:
            return False