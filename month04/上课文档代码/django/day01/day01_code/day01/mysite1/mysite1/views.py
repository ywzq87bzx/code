# 视图函数，参数必须有request，表示Http请求
# 返回值也必须是Http响应
from django.http import HttpResponse


def page_2003(request):
    # 具体的处理业务
    return HttpResponse('这是 page 2003页面！')


def page_2004(request):
    # 具体的处理业务
    return HttpResponse('这是 page 2004 页面')


def default_page(request):
    return HttpResponse('<h1>这是默认首页</h1>')


def page_one(request):
    return HttpResponse('这是编号为1的页面')


def page_num(request, num):
    return HttpResponse('这是编号为%s的页面' % num)


def page_name(request, name):
    return HttpResponse('name is %s' % name)


def math_view(request, a, op, b):

    print(request.path_info)
    print(request.method)
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse('操作符有误！')
    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    return HttpResponse('结果是:%s' % result)


def birthday_view(request, y, m, d):
    # 打印到服务的终端窗口，打印的是path
    print(request.path_info)

    html = '生日为：%s年%s月%s日' % (y, m, d)
    return HttpResponse(html)
