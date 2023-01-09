from rest_framework import permissions
from rest_framework.views import Request, View
from sheet.models import Sheet
import ipdb


class IsSheetOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Sheet):
        return request.user == obj.trainer


class IsTrainer(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_staff
