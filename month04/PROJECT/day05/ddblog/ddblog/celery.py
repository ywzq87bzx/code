from celery import Celery
from django.conf import settings
import os

# 1 添加环境变量,告诉celery为哪个Django项目服务
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ddblog.settings')
# 2 创建celery对象
app=Celery('ddblog')

#3 配置
app.conf.update(
    BROKER_URL='redis://@127.0.0.1:6379/1'
)
#4 高知Celery去哪些应用下查找任务函数
app.autodiscover_tasks(settings.INSTALLED_APPS)