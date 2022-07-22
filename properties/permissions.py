from rest_framework.permissions import BasePermission

class PropertyPermission(BasePermission):
    def has_permission(self, req, _):
        return self._tokenAuth(req)

    @staticmethod
    def _tokenAuth(req):
        return req.method == "GET" or req.user.is_authenticated