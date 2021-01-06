import json
import html

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from message.models import Message
from tools.login_dec import login_check
from tools.login_dec import get_user_by_request
# Create your views here.
from django.views import View

from topic.models import Topic

from user.models import UserProfile
from tools.cache_dec import topic_cache


class TopicViews(View):
    def clear_topic_cache(self, request):
        path = request.path_info
        print(path)
        all_key_p = ['topic_cache_self_', 'topic_cache_']
        all_keys = []
        for key_p in all_key_p:
            for key_h in ['', '?category=tec', '?category=no-tec']:
                all_keys.append(key_p + path + key_h)
        print(all_keys)
        cache.delete_many(all_keys)

    def make_topic_res(self, author, author_topic, is_self):
        if is_self:
            #     不用增加权限条件
            next_topic = Topic.objects.filter(id__gt=author_topic.id, user_profile_id=author.username).first()
            last_topic = Topic.objects.filter(id__lt=author_topic.id, user_profile_id=author.username).last()
        else:
            #     条件增加limit='public'
            next_topic = Topic.objects.filter(id__gt=author_topic.id, user_profile_id=author.username,
                                              limit='public').first()
            last_topic = Topic.objects.filter(id__lt=author_topic.id, user_profile_id=author.username,
                                              limit='public').last()
        if next_topic:
            next_id = next_topic.id
            next_title = next_topic.title
        else:
            next_id = None
            next_title = None
        if last_topic:
            last_id = last_topic.id
            last_title = last_topic.title
        else:
            last_id = None
            last_title = None

        result = {'code': 200, 'data': {}}
        result['data']['nickname'] = author.nickname
        result['data']['title'] = author_topic.title
        result['data']['category'] = author_topic.category
        result['data']['content'] = author_topic.content
        result['data']['introduce'] = author_topic.introduce
        result['data']['author'] = author.nickname
        result['data']['created_time'] = author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
        result['data']['last_id'] = last_id
        result['data']['last_title'] = last_title
        result['data']['next_id'] = next_id
        result['data']['next_title'] = next_title

        # 评论相关
        # 获取该文章的所有评论
        all_messages = Message.objects.filter(topic=author_topic).order_by('-created_time')
        # 存储目标数据
        msg_list = []
        # 存储评论，相当于队员
        r_dict = {}
        # 存储评论数量
        msg_count = 0
        for msg in all_messages:
            if msg.parent_message:
                # 相当于队员
                r_dict.setdefault(msg.parent_message, [])
                r_dict[msg.parent_message].append({
                    'msg_id': msg.id,
                    'content': msg.content,
                    'publisher': msg.user_profile.nickname,
                    'publisher_avatar': str(msg.user_profile.avatar),
                    'created_time': msg.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                })
            else:
                msg_count += 1
                msg_list.append({
                    'id': msg.id,
                    'content': msg.content,
                    'publisher': msg.user_profile.nickname,
                    'publisher_avatar': str(msg.user_profile.avatar),
                    'created_time': msg.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'reply': []
                })
                for m in msg_list:
                    if m['id'] in r_dict:
                        m['reply'] = r_dict[m['id']]

        result['data']['messages'] = msg_list
        result['data']['messages_count'] = msg_count
        return result

    def make_topics_res(self, author, author_topics):
        topics_res = []
        for topic in author_topics:
            d = {}
            d['id'] = topic.id
            d['title'] = topic.title
            d['category'] = topic.category
            d['introduce'] = topic.introduce
            d['created_time'] = topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
            d['author'] = author.username
            topics_res.append(d)

        res = {'code': 200, 'data': {}}
        res['data']['topics'] = topics_res
        res['data']['nickname'] = author.username

        return res

    @method_decorator(login_check)
    def post(self, request, author_id):
        # 获取前段提交的数据
        json_str = request.body
        py_obj = json.loads(json_str)
        content = py_obj['content']
        content_text = py_obj['content_text']
        introduce = content_text[:30]
        # 防止xss攻击
        title = html.escape(py_obj['title'])
        limit = py_obj['limit']
        if limit not in ['public', 'private']:
            result = {'code': 10300, 'error': 'the category is erro'}
            return JsonResponse(result)
        category = py_obj['category']
        # 文章作者
        print(content, content_text, limit, title, category)
        author = request.myuser

        topic = Topic.objects.create(title=title, category=category
                                     , limit=limit, introduce=introduce
                                     , content=content, user_profile=author)
        self.clear_topic_cache(request)
        return JsonResponse({'code': 200, 'username': author.username})

    @method_decorator(topic_cache(600))
    def get(self, request, author_id):
        print('- inview -')
        # 从查询字符串中获取分类
        try:
            author = UserProfile.objects.get(username=author_id)
        except:
            result = {"code": 10305, 'error': 'the user id is error'}
            return JsonResponse(result)
        # 从token中获取登录用户信息
        visitor_name = get_user_by_request(request)

        t_id = request.GET.get('t_id')
        is_self = False
        if t_id:
            # 　文章详情页
            if visitor_name == author_id:
                is_self = True
                try:
                    author_topic = Topic.objects.get(id=t_id, user_profile_id=author_id)
                except:
                    result = {'code': 10310, 'error': 'the topic id is error'}
                    return JsonResponse(result)
            else:
                #  非博主访问
                try:
                    author_topic = Topic.objects.get(id=t_id, user_profile_id=author_id,
                                                     limit='public')
                except:
                    result = {'code': 10310, 'error': 'the topic id is error'}
                    return JsonResponse(result)
            res = self.make_topic_res(author, author_topic, is_self)
            return JsonResponse(res)
        else:
            # 文章列表页
            category = request.GET.get('category')
            filter_category = False
            if category in ['tec', 'no-tec']:
                filter_category = True
            if visitor_name == author_id:
                if filter_category:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, category=category)
                else:
                    author_topics = Topic.objects.filter(user_profile_id=author_id)
            else:
                if filter_category:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, limit='public', category=category)
                else:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, limit='public')

            res = self.make_topics_res(author, author_topics)
            return JsonResponse(res)
