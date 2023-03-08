from django.shortcuts import render

# Create your views here.

# coding: utf-8

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .service import AccountPermission
import common


def login(request):
    # GET页面请求
    if request.method == 'GET':
        token = request.COOKIES.get(common.Cookie_Token)
        if AccountPermission().tokenVerify(token):
            return redirect(common.PageHome)
        else:
            return render(request, 'login.html')

    if 'POST' == request.method:  # 密码验证 前端需要传来三个参数
        username = request.POST['username']
        password = request.POST['password']
        token = AccountPermission().loginVerify(username, password)
        if token:
            response = redirect(common.PageHome)
            response.set_cookie(common.Cookie_Token, token, expires=common.TokenExpired)
            return response
        else:
            return HttpResponse('login failed!')


def home(request):
    token = request.COOKIES.get(common.Cookie_Token)
    print("token", token)
    response = render(request, 'home.html')
    return response
