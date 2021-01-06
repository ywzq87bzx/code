from django.http import JsonResponse
import jwt
from django.conf import settings
from user.models import UserProfile

def login_check(func):
    def wrap(request,*args,**kwargs):
    #     从用户请求中获取token
        token=request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result={'code':403,'error':'请登录'}
            return JsonResponse(result)
        try:
            payload=jwt.decode(token,settings.JWT_TOKEN_KEY,algorithms='HS256')
        except:
            result = {'code': 403, 'error': '请登录'}
            return JsonResponse(result)
        username=payload['username']
        user=UserProfile.objects.get(username=username)
        request.myuser=user
        return func(request,*args,**kwargs)
    return wrap

def get_user_by_request(request):
    token=request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        payload = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms='HS256')
    except:
        return None
    username = payload['username']
    return username