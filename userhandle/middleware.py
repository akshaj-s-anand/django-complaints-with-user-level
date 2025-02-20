from django.core.exceptions import PermissionDenied
import os

class Usermanagement:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_domains = ['127.0.0.1', 'localhost']

    def __call__(self, request):
        host = request.get_host().split(':')[0]
        if host not in self.allowed_domains:
            raise PermissionDenied("YOU ARE TRYING TO DEPLOY THIS PROJECT WITHOUT PERMISSION")
        return self.get_response(request)
