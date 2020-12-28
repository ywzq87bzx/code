from django.http import HttpResponse
from django.shortcuts import render


def test_xhr(request):
    return render(request, 'test_xhr.html')


def test_xhr_get(request):
    return render(request, 'test_xhr_get.html')


def test_xhr_get_server(request):
    return HttpResponse('this is Ajax Data!')


def test_jq_get(request):
    return render(request, 'test_jq_get.html')


def test_jq_get_server(request):
    return HttpResponse('this is Ajax JQ Data!')


def test_json(request):
    return render(request, 'test_json.html')
