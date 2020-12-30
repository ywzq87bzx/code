import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from user.models import UserProfile
import hashlib

import jwt
import time
from django.conf import settings

class UsersView(View):
    def get(self,request):
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
        return JsonResponse({'code':200,'data':{'token':token.decode()}})

def make_token(username,expire=3600*24):
    key=settings.JWT_TOKEN_KEY
    now=time.time()
    payload={'username':username,'exp':now+expire}
    return jwt.encode(payload,key,algorithm='HS256')

