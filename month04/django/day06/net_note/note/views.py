from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from user.models import User
from .models import Note
from time import sleep

# Create your views here.

def login_check(fn):
    def wrap(request,*args,**kwargs):
        if 'uname'not in request.session or 'uid' not in request.session:
            return HttpResponseRedirect('/user/login')
        username=request.session['uname']
        try:
            user=User.objects.get(username=username)
        except Exception as e:
            print('error is %s' % e)
            return HttpResponse('username is error')
        request.myuser=user
        return fn(request,*args,**kwargs)
    return wrap


@login_check
def list_view(request):
    user=request.myuser
    notes=Note.objects.filter(user=user)
    return render(request,'note/list_note.html',locals())


@login_check
def add_view(request):
    if request.method=='GET':
        return render(request, 'note/add_note.html')
    elif request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        user=request.myuser
        #XSS攻击
        #数据入库
        Note.objects.create(title=title,content=content,user=user)
        # sleep(3)
        return HttpResponseRedirect('/note/')



def mod_view(request,id):
    try:
        note=Note.objects.get(id=id)
    except Exception as e:
        print('error is %s' %e)
        return  HttpResponse('note id is error')
    if request.method=='GET':
        return render(request, 'note/mod_note.html',locals())
    elif request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        note.title=title
        note.content=content
        note.save()
        return HttpResponseRedirect('/note/')

@login_check
def del_view(request,id):
    try:
        note = Note.objects.get(id=id)
        note.delete()
    except Exception as e:
        print('error is %s' % e)
        return HttpResponse('note id is error')

    return HttpResponseRedirect('/note/')


