from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.metmod in SAFE_METHODS:
            return True
        elif obj.user == request.user:
            return True
        else:
            return False
        # return super().has_object_permission(request, view, obj)