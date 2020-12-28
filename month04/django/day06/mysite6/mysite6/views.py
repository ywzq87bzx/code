from django.http import HttpResponse


def set_cookie(request):
    resp=HttpResponse('set cookie is ok!')
    resp.set_cookie('uname','aid2009',60)
    return  resp


def get_cookie(request):
    uname=request.COOKIES.get('uname','no value')
    html='uname is %s' % uname
    return HttpResponse(html)


def del_cookie(request):
    resp=HttpResponse('del cookie is ok!')
    resp.delete_cookie('uname')
    return resp

def set_session(request):
    request.session['uname']='aid2009'
    return HttpResponse('set session is ok!')

def get_session(request):
    uname=request.session.get('uname','no value')
    html='uname is %s' % uname
    return HttpResponse(html)

def del_session(request):
    if request.session['uname']:
        del request.session['uname']
    return HttpResponse('del session is ok !')
