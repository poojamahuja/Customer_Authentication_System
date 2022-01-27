from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        # print(user)

        if user.is_customer or user.is_superuser:
            return True
        return False
