



import time
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(20)
def test_cache(request):
    time.sleep(5)
    t1=time.time()
    print('---view in ---')
    return HttpResponse('t1 is %s' %t1)

def test_mw(request):
    print('-----mw view in')
    return HttpResponse('my mw view!')

def test(request):
    print('-----mw view in')
    return HttpResponse('my mw view!')
