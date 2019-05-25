from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAuthorOrSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser
