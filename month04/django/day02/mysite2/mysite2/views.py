from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

html = '''
<form method='get' action="/test_get">
    姓名:<input type="text" name="uname">
    <input type='submit' value='提交'>
</form>

'''


def test_get(request):
    uname = request.GET.get('uname')
    print(uname)

    a = request.GET.get('a')
    print(a)

    b = request.GET.get('b')
    print(b)

    a = request.GET.getlist('a')
    print(a)

    return HttpResponse(html)


html2 = '''
<form method='POST' action="/test_get_post">
    姓名:<input type="text" name="uname">
    <input type='submit' value='提交'>
</form>

'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return '姓名：%s,age：%s' % (self.name, self.age)


def hello():
    return '北京欢迎你'


def test_get_post(request):
    if request.method == 'GET':
        return HttpResponse(html2)
    elif request.method == 'POST':
        # uname = request.POST['uname']
        uname = request.POST.get('uname', '未命名')
        return HttpResponse('数据已提交，uname:%s' % uname)


def test_html(request):
    # t = loader.get_template('test_html.html')
    # html3 = t.render()
    # return HttpResponse(html3)
    # d = {}
    # d['name'] = 'aid2009班'
    # d['count'] = 500
    # d['city'] = ['北京', '上海', '西安']
    # d['score'] = {'python': 99, 'django': 100}
    # d['person'] = Person('宋小宝', 40)
    # d['func1'] = hello
    # d['script'] = '<script>alert(111)</script>'

    name = 'aid2009班'
    count = 500
    city = ['北京', '上海', '西安']
    score = {'python': 99, 'django': 100}
    person = Person('宋小宝', 40)
    func1 = hello
    script = '<script>alert(111)</script>'

    lst = {'关', '张', '赵', '马'}
    # lst = {}
    return render(request, 'test_html.html', locals())


def mycal_view(request):
    if request.method == 'GET':
        return render(request, 'mycalc.html')
    elif request.method == 'POST':
        a = request.POST.get('x')
        b = request.POST.get('y')
        if not a or not b:
            return HttpResponse("请输入数据")
        try:
            a = int(a)
            b = int(b)
        except Exception as e:
            return HttpResponse('error is %s' % e)
        op = request.POST['op']
        result = 0
        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            result = a / b
    # print(locals())
    return render(request, 'mycalc.html', locals())


def birthday(request, y, m, d):
    return HttpResponse('生日为：%s年%s月%s日' % (y, m, d))


def birthday01(request):
    y = request.GET.get('y')
    m = request.GET.get('m')
    d = request.GET.get('d')
    return HttpResponse('生日为：%s年%s月%s日' % (y, m, d))
