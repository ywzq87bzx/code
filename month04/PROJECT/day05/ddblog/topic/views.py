import json
import html

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from tools.login_dec import login_check
from tools.login_dec import get_user_by_request
# Create your views here.
from django.views import View

from topic.models import Topic

from user.models import UserProfile







class TopicViews(View):

    def make_topics_res(self,author,author_topics):
        topics_res=[]
        for topic in author_topics:
            d={}
            d['id']=topic.id
            d['title']=topic.title
            d['category']=topic.category
            d['introduce']=topic.introduce
            d['created_time']=topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
            d['author']=author.username
            topics_res.append(d)

        res= {'code':200,'data':{}}
        res['data']['topics']=topics_res
        res['data']['nickname']=author.username

        return res





    @method_decorator(login_check)
    def post(self,request,author_id):
        # 获取前段提交的数据
        json_str = request.body
        py_obj = json.loads(json_str)
        content = py_obj['content']
        content_text = py_obj['content_text']
        introduce=content_text[:30]
        # 防止xss攻击
        title = html.escape(py_obj['title'])
        limit = py_obj['limit']
        if limit not in ['public','private']:
            result={'code':10300,'error':'the category is erro'}
            return JsonResponse(result)
        category = py_obj['category']
        #文章作者
        print(content, content_text, limit,title,category)
        author = request.myuser


        topic=Topic.objects.create(title=title,category=category
                                       ,limit=limit,introduce=introduce
                                       ,content=content,user_profile=author)

        return JsonResponse({'code':200,'username':author.username})

    def get(self,request,author_id):
        # 从查询字符串中获取分类

        category=request.GET.get('category')
        filter_category = False
        if category in ['tec','no-tec']:
            filter_category=True


        try:
            author=UserProfile.objects.get(username=author_id)
        except:
            result={"code":10305,'error':'the user id is error'}
            return JsonResponse(result)
        visitor_name=get_user_by_request(request)
        if visitor_name==author_id:
            if filter_category:
                author_topics=Topic.objects.filter(user_profile_id=author_id,category=category)
            else:
                author_topics=Topic.objects.filter(user_profile_id=author_id)
        else:
            if filter_category:
                author_topics=Topic.objects.filter(user_profile_id=author_id,limit='public',category=category)
            else:
                author_topics=Topic.objects.filter(user_profile_id=author_id,limit='public')

        res=self.make_topics_res(author,author_topics)
        return JsonResponse(res)









