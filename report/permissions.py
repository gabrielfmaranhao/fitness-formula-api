from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Report
from ..user.models import User
from ..sheet.models import Sheet
class IsUserReport(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:  
        if request.user == user and request.method in permissions.SAFE_METHODS:
            return True 

class IsTrainerReport(permissions.BasePermission):
    def has_object_permission(self, request, view, sheet: Sheet) -> bool:
        return request.trainer == sheet
        