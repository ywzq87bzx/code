from django.db import models


# Create your models here.
class Book(models.Model):
    # 创建一个字符串类型的属性
    # 第一个参数在后台管理页面中使用
    # 第二个参数是必填参数，表示字符串最大长度
    title = models.CharField('书名', max_length=50)
    # 创建一个小数类型的属性
    # 第一个参数在后台管理页面中使用
    # 第二和第三个参数必填参数，max_digits是有效数字长度，
    # decimal_places是小数点后保留几位
    price = models.DecimalField('定价',
                                max_digits=5,
                                decimal_places=2)
    # 新增字段
    # 新增字段要么可以为空，要么有默认值
    pub = models.CharField('出版社',max_length=50,
                           default='')
    market_price = models.DecimalField('零售价',
                                       max_digits=5,
                                       decimal_places=2,
                                       default=0.0)
    # 内部类
    class Meta:
        db_table = 'book'

