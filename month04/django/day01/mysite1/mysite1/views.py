from django.http import HttpResponse


def page_1(request):
    return HttpResponse('<h1>这是编号为1的页面！</h1>')


def page_2(request):
    return HttpResponse('这是编号为2的页面！')


def page(request):
    return HttpResponse('这是我的首页')


def page_num(request, num):
    return HttpResponse('这是%d页面' % num)


def page_name(request, name):
    return HttpResponse('这是%d页面' % name)


def page_cul(request, a, op, b):
    print(request.path_info)
    if op == 'add':
        return HttpResponse(a + b)
    elif op == 'sub':
        return HttpResponse(a - b)
    elif op == 'mul':
        return HttpResponse(a * b)


def callview(request, y, m, d):
    print(request.path_info, request.method)

    html = '生日为：%s年%s月%s日' % (y, m, d)
    return HttpResponse(html)
