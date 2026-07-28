from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status

class RolePermission(BasePermission):
    """
    Usage: RolePermission(allowed_roles=['employer','admin'])
    Provide allowed_roles attribute on the view or pass it when instantiating.
    """
    def has_permission(self, request, view):
        allowed = getattr(view, 'allowed_roles', None)
        if allowed is None:
            return True
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.role in allowed
