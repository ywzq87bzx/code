from django.http import HttpResponse
from django.shortcuts import render
from user.models import User
# Create your views here.

import redis

r = redis.Redis(password='123456')


def user_detail(request, id):
    cache_key = 'user_%s' % id
    if r.exists(cache_key):
        data=r.hgetall(cache_key)
        print(data)
        new_data={k.decode():v.decode() for k,v in data.items()}
        username=new_data['username']
        age=new_data['age']
        html='cache:username is %s,age is %s'%(username,age)
        return HttpResponse(html)
    else:
        try:
            user=User.objects.get(id=id)
        except Exception as e:
            return HttpResponse('user id is error')
        r.hmset(cache_key,{'username':user.username,'age':user.age})
        r.expire(cache_key,60)
        html='mysql:username is %s,age is %s'%(user.username,user.age)
        return HttpResponse(html)


def user_update(request,id):
    age=request.GET.get('age',0)
    try:
        user=User.objects.get(id=id)
    except:
        return HttpResponse('user id is error')
    user.age=age
    user.save()
    cache_key='user_%s'%id
    r.delete(cache_key)
    return  HttpResponse('update user is ok')
