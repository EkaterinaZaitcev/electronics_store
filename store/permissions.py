from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """Ограничение доступа к ресурсам"""

    def has_object_permission(self, request, view, obj):
        if request.user.is_active:
            return True
        return False
