from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField('书名',max_length=50)
    price=models.DecimalField('定价',max_digits=5,decimal_places=2)
    pub=models.CharField('出版社',max_length=5,default='')
    market_price=models.DecimalField('零售价',max_digits=5,decimal_places=2,default=0.0)

    class Meta:
        db_table='book'

class Author(models.Model):
    name=models.CharField('姓名',blank=False,max_length=5)
    age=models.IntegerField('年纪',null=False,default=1)
    email=models.EmailField('邮箱',max_length=20)
    class Meta:
        db_table='Author'