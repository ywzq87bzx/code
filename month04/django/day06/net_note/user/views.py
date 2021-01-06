import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User


# Create your views here.


def login_view(request):
    if request.method == 'GET':
        if 'uname' in request.session and 'uid' in request.session:
            # return HttpResponse
            return HttpResponseRedirect('/note/')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            old_user = User.objects.get(username=username)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse('用户名或密码错误！')
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != old_user.password:
            return HttpResponse('用户名或密码错误！')

        request.session['uname'] = old_user.username
        request.session['uid'] = old_user.id

        # return HttpResponse('登录成功！')
        return HttpResponseRedirect('/note/')


def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        if not username or not password_1:
            return HttpResponse('用户名和密码不允许为空')
        if password_1 != password_2:
            return HttpResponse('两次密码要一致')
        old_user = User.objects.filter(username=username)
        if old_user:
            return HttpResponse("用户名已经存在")
        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_h = md5.hexdigest()
        # 数据入库
        try:
            User.objects.create(username=username, password=password_h)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse('用户名已经存在')
        return HttpResponse('用户注册成功！')


def logout_view(request):
    if 'uname' in request.session:
        del request.session['uname']
    if 'uid' in request.session:
        del request.session['uid']
    return HttpResponse('用户退出成功！')
