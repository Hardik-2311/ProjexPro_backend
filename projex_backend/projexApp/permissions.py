from rest_framework import permissions

class IsYearGreaterThanTwo(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.year >= 2
        return False
class onlyProjectView(IsYearGreaterThanTwo):
    def has_permission(self, request, view):
        if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return super().has_permission(request, view)
        return True
