from django.core.cache import cache

from .login_dec import get_user_by_request


def topic_cache(expire):
    def _topic_cache(func):
        def wrapper(request,*args,**kwargs):
            if 't_id' in request.GET.keys():
                return func(request,*args,**kwargs)
            visitor_name=get_user_by_request(request)
            author_name=kwargs['author_id']
            if visitor_name==author_name:
                cache_key='topic_cache_self_%s'%(request.get_full_path())
            else:
                cache_key = 'topic_cache_%s'%(request.get_full_path())
            print('cache_key is %s'%cache_key)

            res=cache.get(cache_key)
            if res:
                print('-cache in -')
                return res
            res=func(request,*args,**kwargs)
            cache.set(cache_key,res,expire)
            return res
        return wrapper
    return _topic_cache
