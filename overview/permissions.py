from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Overview
import ipdb

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.user.is_authenticated:
            return True

        return False

class IsStaff(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.user.is_authenticated and request.user.is_staff:
            return True

        return False

class IsStaffOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Overview):
        return obj.created_by == request.user