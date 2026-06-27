from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsProjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True 
        return obj.owner == request.user
       
class IsTaskOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if obj.project.owner == request.user:
            return True
        if obj.assigned_to == request.user:
            if request.method =='PATCH':
                return True
        return False
        
        

    