from django.db import models


# Create your models here.
class Content(models.Model):
    title = models.CharField('文件描述', max_length=50)
    # 第一个参数，会在media目录下，再创建一个子目录myfiles
    # 所有与这个模型类相关的上传的文件都放到该目录下
    myfile = models.FileField(upload_to='myfiles')
