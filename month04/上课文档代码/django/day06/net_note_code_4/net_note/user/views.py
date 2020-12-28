from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib


# Create your views here.

def login_view(request):
    if request.method == 'GET':
        if 'uname' in request.session and 'uid' in request.session:
            # 实际可以跳转到登录后，操作页面
            #return HttpResponse('您已经登录了')
            return HttpResponseRedirect('/note/')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 1 获取用户输入
        username = request.POST['username']
        password = request.POST['password']
        # 2 查看username用户是否存在
        try:
            old_user = User.objects.get(username=username)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse('用户名或密码错误！')
        # 3 比较密码
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != old_user.password:
            return HttpResponse('用户名或密码错误！')
        # 登录成功后，将用户信息存储在session中
        request.session['uname'] = old_user.username
        request.session['uid'] = old_user.id
        # 4 返回响应
        # return HttpResponse("登录成功！")
        return HttpResponseRedirect('/note/')


def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # 1 获取用户输入的值
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        # 2 为空判断
        if not username or not password_1:
            return HttpResponse('用户名和密码不允许为空')
        # 3 两次密码要一致
        if password_1 != password_2:
            return HttpResponse('两次密码要一致！')
        # 4 用户名是否被占用
        old_user = User.objects.filter(username=username)
        if old_user:
            return HttpResponse('用户名已被占用')

        # 5 计算用户输入的密码的Hash值
        md5 = hashlib.md5()
        # password_1是字符串类型，update参数要求是字节串
        # 所以需要调用encode()做一下转换
        md5.update(password_1.encode())
        password_h = md5.hexdigest()
        # 6 数据入库
        try:
            User.objects.create(username=username,
                                password=password_h)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse('用户名已被占用')
        return HttpResponse('用户注册成功！')


def logout_view(request):
    # 用户退出/注销实则是把用户登录的状态信息从session或cookies中删除
    if 'uname' in request.session:
        del request.session['uname']
    if 'uid' in request.session:
        del request.session['uid']
    return HttpResponse('用户退出成功！')
