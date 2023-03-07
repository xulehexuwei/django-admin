from django.shortcuts import render

# Create your views here.

# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect

# def login(request):
#     # return HttpResponse("Hello world ! ")
#     return render(request, 'login.html') #上传index.html文件到templates目录下

def login(request):
    if 'GET' == request.method: #GET页面请求
        try : #尝试获取请求中GET的next参数，并且构成上写文
            next=request.GET['next'] #注意这里用try，因为当请求不包含next时，比如直接访问登录页面，GET['next']并不存在，会发生错误
            context = {
                'next':next
            }
        except :
            context={
            'next':'/auth/home/' #如果没有next，制定next为主页面
            }
        return render(request,'login.html', context=context)

    if 'POST'== request.method: #密码验证 前端需要传来三个参数
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']

        # user = authenticate(request, username=username, password=password)
        if username == "xuwei":
            user = "xuwei"
        else:
            user = None

        if user is not None:
            # login(request, user)
            #redirect to a success page.
            return HttpResponseRedirect(next)
        else:
            return HttpResponse('login failed!')


def home(request):
    # return HttpResponse("Hello world ! ")
    return render(request, 'home.html') #上传index.html文件到templates目录下