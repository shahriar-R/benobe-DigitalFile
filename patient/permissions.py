from rest_framework import permissions


class PatientOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.doctor == request.user:
            return True
        return False

class PatientCreate(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        # if request.method in permissions.SAFE_METHODS:
        #     return True

        if obj.doctor == request.user:
            return True

        # if request.user.is_staff and request.method not in self.edit_methods:
        #     return True


        return obj.doctor.user == request.user