from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def list_view(request):
    return render(request, 'note/list_note.html')


def add_view(request):
    return render(request, 'note/add_note.html')


def mod_view(request, id):
    return render(request, 'note/mod_note.html')


def del_view(request, id):
    return HttpResponse('删除成功！')
