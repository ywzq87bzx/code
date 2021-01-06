import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from tools.login_dec import login_check
from topic.models import Topic
from .models import Message


@login_check
def message_view(request,topic_id):
    if request.method!='POST':
        result={'code':10400,'error':'please use POST'}
        return JsonResponse(result)
    json_str=request.body
    py_obj=json.loads(json_str)
    content=py_obj['content']
    parent_id=py_obj.get('parent_id',0)
    try:
        topic=Topic.objects.get(id=topic_id)
    except:
        result={'code':10401,'error':'topic id is error'}
        return JsonResponse(result)

    user=request.myuser
    Message.objects.create(topic=topic,user_profile=user,content=content,
                           parent_message=parent_id)
    return JsonResponse({'code':200})


