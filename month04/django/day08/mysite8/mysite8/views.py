import csv
import os

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from test_upload.models import *
from django.contrib.auth.models import User
from django.core import mail

def test_csrf(request):
    if request.method=='GET':
        return render(request,'test_csrf.html')
    elif request.method=='POST':
        username=request.POST['username']
        return HttpResponse('username is %s' %username)

@csrf_exempt
def test_csrf1(request):
    if request.method=='GET':
        return render(request,'test_csrf1.html')
    elif request.method=='POST':
        return HttpResponse('提交成功')

def test_page(request):
    lst=['a','b','c','d','e']
    piginator=Paginator(lst,2)
    cur_page=request.GET.get('page',1)
    page=piginator.page(cur_page)
    return render(request,'test_page.html',locals())

def test_csv(request):
    username=request.GET.get('username','bzx')
    response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    response['Content-Disposition'] = 'attachment; filename="%s.csv"' % username
    all_book = [
        {'id':1,'title':'python'},
        {'id':2,'title':'c++'},
        {'id':3,'title':'java'},
    ]
    writer = csv.writer(response)
    writer.writerow(['id', 'title'])
    for b in all_book:
        writer.writerow([b['id'], b['title']])
    return response


@csrf_exempt
def test_upload(request):
    if request.method=='GET':
        return  render(request,'test_upload.html')
    elif request.method=='POST':
        title=request.POST['title']
        a_file=request.FILES['myfile']
        print("上传文件名是:", a_file.name)
        filename = os.path.join(settings.MEDIA_ROOT, a_file.name)
        with open(filename, 'wb') as f:
            data = a_file.file.read()
            f.write(data)
        return HttpResponse("接收文件:" + a_file.name + "成功")


@csrf_exempt
def upload_view_dj(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == 'POST':
        title = request.POST['title']
        a_file = request.FILES['myfile']
        Content.objects.create(desc=title,myfile=a_file)
        return HttpResponse('-----文件上传成功------')


@csrf_exempt
def user_reg(request):
    if request.method=='GET':
        return render(request,'user_reg.html')
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_active = True  # 记当前用户活跃
        user.is_staff = True  # 记当前用户活跃

        user.save()
        return HttpResponse('注册后台用户成功')

@csrf_exempt
def mail_view(request):
    if request.method=='GET':
        return render(request, 'user_email.html')
    elif request.method=='POST':
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = request.POST['from_email']
        to_email=[request.POST['to_email']]
        mail.send_mail(subject, message, from_email,to_email)
        return  HttpResponse('发送成功')