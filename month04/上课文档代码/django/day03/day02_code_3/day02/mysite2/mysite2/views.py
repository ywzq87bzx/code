from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

html = '''
<form method='get' action="/test_get">
    姓名:<input type="text" name="uname">
    <input type="submit" value="提交">
</form>
'''


def test_get(request):
    # 获取查询字符串的值
    # uname = request.GET['uname']
    # 温柔的获取查询字符串的值,推荐的方式
    uname = request.GET.get('uname')
    print(uname)
    a = request.GET.get('a')
    print(a)
    b = request.GET.get('b')
    print(b)
    # 可以有缺省值
    c = request.GET.get('c', 300)
    print(c)
    # 如果同一名称有多个值,可以列表的方式获取
    a = request.GET.getlist('a')
    print(a)
    return HttpResponse(html)


html2 = '''
<form method='post' action="/test_get_post">
    姓名:<input type="text" name="uname">
    <input type="submit" value="提交">
</form>
'''


def test_get_post(request):
    if request.method == 'GET':
        return HttpResponse(html2)
    elif request.method == 'POST':
        # 获取表单数据，一般把信息记录到数据库
        # uname = request.POST['uname']
        # 也可以温柔的获取数据
        uname = request.POST.get('uname', '未命名')
        return HttpResponse('您的数据已提交，uname:%s' % uname)


# 定义一个类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return '姓名:%s,age:%s' % (self.name, self.age)


# 定义一个函数
def hello():
    return '北京欢迎您！'


def test_html(request):
    # 方式一
    # # 1 加载模板
    # t = loader.get_template('test_html.html')
    # # 2 将t转换成html字符串
    # html = t.render()
    # # 3 将html作为响应的内容
    # return HttpResponse(html)
    # 方式二 直接加载并响应模板
    # #
    # d = {}
    # d['name'] = 'aid2009 vip 班'
    # d['count'] = 500
    # d['citys'] = ['北京', '上海', '广州', '深圳']
    # d['score'] = {'python': 99, 'django': 100}
    # d['person'] = Person('宋小宝', 40)
    # d['func1'] = hello
    # d['script'] = '<script>alert(111)</script>'
    # return render(request, 'test_html.html', d)
    # 方式三
    name = 'aid2009VIP班'
    count = 199
    citys = ['北京', '上海', '广州', '深圳']
    score = {'python': 99, 'django': 100}
    person = Person('宋小宝', 40)
    func1 = hello
    script = '<script>alert(111)</script>'

    lst = ['关羽', '张飞', '赵云', '马超', '黄忠']
    lst = []
    # locals()自动的将视图函数的局部变量封装成字典
    return render(request, 'test_html.html', locals())


def mycal_view(request):
    if request.method == 'GET':
        # 返回页面
        return render(request, 'mycalc.html')
    elif request.method == 'POST':
        x = request.POST['x']
        y = request.POST.get('y')
        if not x or not y:
            return HttpResponse('请输入数据')
        try:
            x = int(x)
            y = int(y)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse("请输入数值类型")
        op = request.POST['op']
        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        return render(request, 'mycalc.html', locals())


def birthday_view(request, y, m, d):
    return HttpResponse('生日为：%s年%s月%s日' % (y, m, d))


def birthday_view2(request):
    y = request.GET.get('y')
    m = request.GET.get('m')
    d = request.GET.get('d')
    return HttpResponse('生日为：%s年%s月%s日' % (y, m, d))
