from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from user.models import User
from .models import Note


def login_check(fn):
    def wrap(request, *args, **kwargs):
        if 'uname' not in request.session or 'uid' not in request.session:
            return HttpResponseRedirect('/user/login')
        username = request.session['uname']
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse('username is error')
        request.myuser = user
        return fn(request, *args, **kwargs)

    return wrap


# Create your views here.
@login_check
def list_view(request):
    user = request.myuser
    # 属性值=对象  user_id = user.id
    notes = Note.objects.filter(user=user)
    return render(request, 'note/list_note.html', locals())


@login_check
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        # 1 获取用户输入的数据
        title = request.POST['title']
        content = request.POST['content']
        user = request.myuser
        # 2 数据入库
        Note.objects.create(title=title,
                            content=content,
                            user=user)
        # 3 重定向到笔记列表页
        return HttpResponseRedirect('/note/')


@login_check
def mod_view(request, id):
    # 1. 获取要修改的笔记对象
    try:
        note = Note.objects.get(id=id)
    except Exception as e:
        print('error is %s' % e)
        return HttpResponse('note id is error')
    if request.method == 'GET':
        return render(request, 'note/mod_note.html', locals())
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        # 2 修改(属性赋一个新的值)
        note.title = title
        note.content = content
        # 3 保存
        note.save()
        # 4 重定向到列表页
        return HttpResponseRedirect('/note/')


@login_check
def del_view(request, id):
    try:
        note = Note.objects.get(id=id)
        note.delete()
    except Exception as e:
        print('error is %s' % e)
        return HttpResponse('note id is error')
    return HttpResponseRedirect('/note/')
    # return HttpResponse('删除成功！')
