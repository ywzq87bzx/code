import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from tools.login_dec import login_check
from user.models import UserProfile
import hashlib

import jwt
import time
import json
from django.conf import settings


class UsersView(View):
    def get(self,request,username=None):
        if username:
            try:
                user=UserProfile.objects.get(username=username)
            except:
                result={'code':10104,'error':'当前用户不存在'}
                return JsonResponse(result)
            if request.GET.keys():
                data={}
                for k in request.GET.keys():
                    if k=='password':
                        continue
                    if hasattr(user,k):
                        data[k]=getattr(user,k)
                result={'code':200,'username':user.username,
                        'data':data}
            else:
                result={'code':200,'username':user.username,
                    'data':{'info':user.info,'sign':user.sign,
                            'nickname':user.nickname,
                            'avatar':str(user.avatar)
                            }}
            return JsonResponse(result)
        else:
            pass
        return HttpResponse('-user get-')
    def post(self,request):
        json_str=request.body
        py_obj=json.loads(json_str)
        username=py_obj['username']
        email=py_obj['email']
        phone=py_obj['phone']
        password_1=py_obj['password_1']
        password_2=py_obj['password_2']
        # print(username,email,phone,password_1,password_2)
        if len(username)>20:
            result={'code':10100,'error':'用户名长度不能超过20个字符串'}
            return JsonResponse(result)
        if password_1!=password_2:
            result = {'code': 10101, 'error': '两次密码不一致'}
            return JsonResponse(result)
        old_user=UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10102, 'error': '用户名已经存在'}
            return JsonResponse(result)
        md5=hashlib.md5()
        md5.update(password_1.encode())
        password_h=md5.hexdigest()
        try:
            user=UserProfile.objects.create(username=username,email=email,phone=phone,
                                            password=password_h,nickname=username)
        except:
            result = {'code': 10103, 'error': '用户名已经存在'}
            return JsonResponse(result)
        token=make_token(username)
        return JsonResponse({'code':200,'username':username,
                             'data':{'token':token.decode()}})

    @method_decorator(login_check)
    def put(self,request,username):
        json_str=request.body
        py_obj=json.loads(json_str)
        sign=py_obj['sign']
        nickname=py_obj['nickname']
        info=py_obj['info']
        print(sign,nickname,sign)
        user=request.myuser
        user.sign=sign
        user.nickname=nickname
        user.info=info
        user.save()
        result={'code':200,'username':user.username}
        return JsonResponse(result)

def make_token(username,expire=3600*24):
    key=settings.JWT_TOKEN_KEY
    now=time.time()
    payload={'username':username,'exp':now+expire}
    return jwt.encode(payload,key,algorithm='HS256')


@login_check
def user_avatar(request,username):
    if request.method!='POST':
        result={'code':10105,'error':'请发送post请求'}
        return JsonResponse(result)
    user=request.myuser
    user.avatar=request.FILES['avatar']
    user.save()
    result={'code':200,'username':user.username}
    return JsonResponse(result)
