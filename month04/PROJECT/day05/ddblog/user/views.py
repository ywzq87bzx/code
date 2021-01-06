import json
import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .tasks import send_sms

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from tools.login_dec import login_check
from tools.sms import YunTongXin
from user.models import UserProfile
import hashlib
from django.core.cache import cache

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

        #1 获取用户输入验证码(看看前段有没有给你，10分钟）
        sms_num=py_obj['sms_num']
        print('sms_num:%s'% sms_num)
        #2 从redis中获取暂存的验证码
        cache_key='sms_%s'% phone
        cache_code=cache.get(cache_key)
        #3 判断redis中的验证码是否为空？
        if not cache_code:
            result={'code':10110,'error':'验证码已过期'}
            return JsonResponse(result)
        #4 用户输入的和redis中的验证码是否相等？
        if int(sms_num)!=cache_code:
            result={'code':10111,'error':'验证码输入错误'}
            return JsonResponse(result)

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


def sms_view(request):
    json_str=request.body
    py_obj=json.loads(json_str)
    phone=py_obj['phone']
    code=random.randint(1000,9999)
    print(phone,code)
    #1.先验证码暂存，以备注册使用
    cache_key='sms_%s' % phone
    cache.set(cache_key,code,65)
    #
    # #2 发送短信验证码
    # x=YunTongXin(settings.SMS_ACCOUNT_ID,
    #              settings.SMS_ACCOUNT_TOKEN,
    #              settings.SMS_APP_ID,
    #              settings.SMS_TEMPLATE_ID)
    # res=x.run(phone,code)
    # print(res)
    # 异步方式发送
    send_sms.delay(phone,code)

    return JsonResponse({'code':200})
