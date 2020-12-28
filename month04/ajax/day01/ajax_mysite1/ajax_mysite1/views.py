from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json


def test_xhr(request):
    return render(request,'test_xhr.html')
def test_xhr_get(request):
    return render(request, 'test_xhr_get.html')
def test_xhr_get_server(request):
    return HttpResponse('this is Ajax Date')
def test_jq_get(request):
    return render(request, 'test_jq_get.html')

def test_jq_get_server(request):
    return HttpResponse('this is Ajax jq Date')

def test_json(request):
    return render(request,'test_json.html')

def make_json_server(request):
    map1=[{'name':'tedu','age':18},
          {'name':'tedu2','age':20},
          ]
    return JsonResponse(map1,safe=False)


def cross(request):
    return render(request,'cross.html')

def cross_server(request):

    func=request.GET.get('callback')
    return HttpResponse(func+'("我跨域来了")')


def cross_server_json(request):
    func = request.GET.get('callback')
    dict1={'name':'tedu','age':18}
    return HttpResponse(func + "("+ json.dumps(dict1) +")")

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        print(uname,pwd)
        return HttpResponse('注册成功')

