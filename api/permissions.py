from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    # def has_permission(self, request, view):
    #     if request.user.is_staff:
    #        return super().has_permission(request, view)
    #    return False
    #     user=request.user
    #     print(user.get_all_permissions())
    #     if request.user.is_staff:
    #         if user.has_perm("product.add_product"): #"app_name.verb_model_name"
    #             return True
    #         if user.has_perm("product.delete_product"):
    #             return True
    #         if user.has_perm("product.change_product"):
    #             return True
    #         if user.has_perm("product.view_product"):
    #             return True
    #         return False
    #     return False
       