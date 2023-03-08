from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect, render, redirect
import common
from login.service import AccountPermission


class LoginVerify(MiddlewareMixin):
    def process_request(self, request):
        request.jwt_token = None
        token = request.COOKIES.get(common.Cookie_Token)
        # path是登录页的时候直接返回该页面，如果是 HttpResponseRedirect(common.PageLogin) 是形成死循环
        path = request.path
        print("path request: ", path)
        print("token request: ", token)
        if path.startswith(common.PageLogin): return None

        # 没token 登录肯定过期了
        if not token:
            # return HttpResponseRedirect(common.PageLogin)
            return redirect(common.PageLogin)

        ap = AccountPermission()
        token_efficient = ap.tokenVerify(token)
        if token_efficient:
            request.jwt_token = ap.token
            return None
        else:
            return redirect(common.PageLogin)

    def process_response(self, request, response):
        # 刷新token过期时间
        if request.jwt_token:
            response.set_cookie(common.Cookie_Token, request.jwt_token, expires=common.TokenExpired)
            print("token response: ", request.jwt_token)
        return response
