from django.http import HttpResponse
from django.shortcuts import render



def index_view(request):
    return render(request,'base.html')

def news_view(request):
    return render(request,'nesws.html')
def sports_view(request):
    return render(request,'sports.html')

def pagen_view(request,n):
    return HttpResponse('%s'%n)

def test_static(request):
    return render(request,'test_static.html')
