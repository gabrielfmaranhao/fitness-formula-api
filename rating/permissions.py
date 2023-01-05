from rest_framework import permissions

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.user.is_staff is False:
            return True

        return False