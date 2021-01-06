from django.db import models
from topic.models import Topic
# Create your models here.
from user.models import UserProfile


class Message(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    user_profile=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    content=models.CharField('内容',max_length=50)
    created_time=models.DateTimeField(auto_now_add=True)
    parent_message=models.IntegerField('哪个评论的回复',default=0)