from rest_framework import permissions

class IsTrainer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff == True 