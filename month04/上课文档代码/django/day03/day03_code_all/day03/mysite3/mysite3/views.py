from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index_view(request):
    name = 'aid2009'
    return render(request, 'base.html', locals())


def news_view(request):
    return render(request, 'news.html')


def sports_view(request):
    return render(request, 'sports.html')


def pagen_view(request, n):
    # 将url名称反向解析出他的值
    url_value = reverse('pgn_url', args=[300])
    print(url_value)
    return HttpResponse('this is page %s' % n)


def test_static(request):
    return render(request, 'test_static.html')
