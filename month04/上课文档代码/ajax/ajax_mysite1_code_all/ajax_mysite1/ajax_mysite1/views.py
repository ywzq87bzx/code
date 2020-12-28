from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def test_xhr(request):
    return render(request, 'test_xhr.html')


def test_xhr_get(request):
    return render(request, 'test_xhr_get.html')


def test_xhr_get_server(request):
    return HttpResponse('this is Ajax Data!')


def test_jq_get(request):
    return render(request, 'test_jq_get.html')


def test_jq_get_server(request):
    return HttpResponse('this is Ajax JQ Data!')


def test_json(request):
    return render(request, 'test_json.html')


def make_json_server(request):
    # 1 字典类型不需要设置第二个参数
    # map1 = {'name': 'tedu', 'age': 18}
    # return JsonResponse(map1)

    # 2 列表或元组需要将safe参数设置为False
    list1 = [
        {'name': 'tedu', 'age': 18},
        {'name': 'tedu2', 'age': 20},
    ]
    return JsonResponse(list1, safe=False)


def cross(request):
    return render(request, 'cross.html')


def cross_server(request):
    func = request.GET.get('callback')
    # print("我跨域来了");
    return HttpResponse(func + '("我跨域来了")')


import json


def cross_server_json(request):
    func = request.GET.get('callback')
    dict1 = {'name': 'tedu', 'age': 18}
    return HttpResponse(func + "(" + json.dumps(dict1) + ")")


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # 获取前端提交的数据
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        print(uname, pwd)
        # 实际应该将数据保存到数据库

        return HttpResponse("%s注册成功！" % uname)
