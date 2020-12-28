from django.http import HttpResponse
from django.shortcuts import render

import redis
from .models import User

# 1 创建redis对象
r = redis.Redis(password='123456')


# Create your views here.
def user_detail(request, id):
    cache_key = 'user_%s' % id
    # 判断缓存中是否有数据redis
    if r.exists(cache_key):
        # 1有，读取redis中的数据，并响应【快】
        data = r.hgetall(cache_key)
        # {b'username': b'tedu', b'age': b'18'}
        print(data)
        # 字节串转字符串
        new_data = {k.decode(): v.decode() for k, v in data.items()}
        username = new_data['username']
        age = new_data['age']
        html = 'cache:username is %s,age is %s' % (username, age)
        return HttpResponse(html)
    else:
        # 2没有，读取mysql中的数据，写入redis，并响应【慢】
        try:
            user = User.objects.get(id=id)
        except Exception as e:
            return HttpResponse('user id is error')
        r.hmset(cache_key, {'username': user.username, 'age': user.age})
        r.expire(cache_key, 300)
        html = 'mysql:username is %s,age is %s' % (user.username,
                                                   user.age)
        return HttpResponse(html)


def user_update(request, id):
    age = request.GET.get('age',0)
    try:
        user = User.objects.get(id=id)
    except:
        return HttpResponse('-user id is error-')
    user.age = age
    user.save()
    cache_key = 'user_%s' % id
    r.delete(cache_key)
    return HttpResponse('-update user is OK!-')
