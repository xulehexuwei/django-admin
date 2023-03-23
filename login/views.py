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
        try:  # 尝试获取请求中GET的next参数，并且构成上写文
            next = request.GET['next']  # 注意这里用try，因为当请求不包含next时，比如直接访问登录页面，GET['next']并不存在，会发生错误
            context = {
                'next': next
            }
        except:
            context = {
                'next': common.PageHome  # 如果没有next，制定next为主页面
            }

        token = request.COOKIES.get(common.Cookie_Token)
        ap = AccountPermission()
        token_efficient = ap.tokenVerify(token)
        if token_efficient:
            response = redirect(context["next"])
            response.set_cookie(common.Cookie_Token, ap.token, expires=common.TokenExpired)
            return response
        else:
            return render(request, 'login.html', context=context)

    if 'POST' == request.method:  # 密码验证 前端需要传来三个参数
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']

        token = AccountPermission().loginVerify(username, password)
        if token:
            response = redirect(next)
            response.set_cookie(common.Cookie_Token, token, expires=common.TokenExpired)
            return response
        else:
            return HttpResponse('login failed!')


def home(request):
    response = render(request, 'home.html')
    return response


def news(request):
    response = render(request, 'news.html')
    return response

def neo4j(request):
    response = render(request, 'neo4jd3.html')
    return response