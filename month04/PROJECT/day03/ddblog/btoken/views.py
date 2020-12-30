import json
import hashlib

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from user.models import UserProfile
from user.views import make_token


class TokenView(View):
    def get(self,request):
        return HttpResponse('get token')

    def post(self,request):
        json_str=request.body
        py_obj=json.loads(json_str)
        username=py_obj['username']
        password=py_obj['password']
        # print(username,password)
        try:
            user=UserProfile.objects.get(username=username)
        except:
            result= {'code':10200,'error':'用户名密码错误'}
            return JsonResponse(result)
        md5=hashlib.md5()
        md5.update(password.encode())
        password_h=md5.hexdigest()
        if password_h!=user.password:
            result = {'code': 10201, 'error': '用户名密码错误'}
            return JsonResponse(result)
        token=make_token(username)
        return JsonResponse({'code':200,'username':username,
                             'data': {'token': token.decode()}
                             })