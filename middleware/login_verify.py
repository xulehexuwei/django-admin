from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect
import common
from login.service import AccountPermission


class LoginVerify(MiddlewareMixin):
    def process_request(self, request):
        token = request.COOKIES.get(common.Cookie_Token)
        request.jwt_token = token

        # path是登录页的时候直接返回该页面，如果是 HttpResponseRedirect(common.PageLogin) 是形成死循环
        path = request.path
        if path.startswith(common.PageLogin): return None

        # 没token 登录肯定过期了
        if not token: return HttpResponseRedirect(common.PageLogin)

        ap = AccountPermission()
        token_efficient = ap.tokenVerify(token)
        if token_efficient:
            request.jwt_token = ap.token
            return None
        else:
            return HttpResponseRedirect(common.PageLogin)

    def process_response(self, request, response):
        # 刷新token过期时间
        if request.jwt_token:
            response.set_cookie(common.Cookie_Token, request.jwt_token, expires=common.TokenExpired)
        return response
