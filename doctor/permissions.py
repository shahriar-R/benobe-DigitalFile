from rest_framework import permissions


class IsDoctorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        # if .objects.filter(ip_addr=ip_addr).exists():
        #     return True
        if obj.doctor == request.user:
            return True


        return False