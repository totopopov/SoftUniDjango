from rest_framework.permissions import BasePermission


class IsAnonymous(BasePermission):

    def has_permission(self, request, view):
        return True if request.user.is_anonymous else False


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
