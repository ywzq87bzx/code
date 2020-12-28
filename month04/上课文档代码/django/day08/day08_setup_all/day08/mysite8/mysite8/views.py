from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

import csv

from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from test_upload.models import Content

def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        username = request.POST['username']
        return HttpResponse('username is %s' % username)


def test_page(request):
    # 1 要分页的数据
    lst = ['a', 'b', 'c', 'd', 'e']
    # 2 创建分页对象
    paginator = Paginator(lst, 2)
    # 3 获取当前页码
    cur_page = request.GET.get('page', 1)
    # 4 获取具体的page对象
    page = paginator.page(cur_page)
    return render(request, 'test_page.html', locals())


def test_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    all_book = [
        {'id': 1, 'title': 'python'},
        {'id': 2, 'title': 'c++'},
        {'id': 3, 'title': 'Java'}
    ]
    writer = csv.writer(response)
    writer.writerow(['编号', '书名'])
    for book in all_book:
        writer.writerow([book['id'], book['title']])
    return response


@csrf_exempt
def test_upload(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == 'POST':
        # 1  获取文件对象
        title = request.POST['title']
        afile = request.FILES['myfile']

        # 方式 1： python的上传文件方式
        # 2 服务器端文件的绝对路径（全路径）
        # filename = os.path.join(settings.MEDIA_ROOT,
        #                         afile.name)
        # with open(filename, 'wb') as f:
        #     data = afile.file.read()
        #     f.write(data)
        # return HttpResponse('上传文件成功！文件名称:%s,标题:%s' % (afile.name,
        #                                               title))
        # 方式2： Django的方式上传文件【推荐的方式】
        Content.objects.create(title=title,myfile=afile)
        return HttpResponse('文件上传成功！')

