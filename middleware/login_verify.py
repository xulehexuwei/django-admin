from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect
from common import router


class LoginVerify(MiddlewareMixin):
    def process_request(self, request):
        path = request.path
        print(path)
        if path.startswith(router.PageLogin):
            return None
        token = request.COOKIES.get('token')
        # TODO 验证token
        if not token:
            return HttpResponseRedirect(router.PageLogin)
        else:
            return None

    def process_response(self, request, response):
        return response
