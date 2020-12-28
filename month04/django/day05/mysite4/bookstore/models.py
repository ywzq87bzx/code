from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField('书名',max_length=30)
    price=models.DecimalField('定价',max_digits=5,decimal_places=2)
    market_price=models.DecimalField('零售价',max_digits=5,decimal_places=2)
    pub=models.CharField('出版社',max_length=30)
    def __str__(self):
        return '%s_%s_%s_%s' %(self.title,
                               self.price,
                               self.market_price,
                               self.pub)
    class Meta:
        verbose_name = '图书'
        verbose_name_plural='图书'

class Author(models.Model):
    name = models.CharField('姓名', max_length=30)
    age = models.IntegerField('年龄', max_length=3)
    def __str__(self):
        return '%s_%s' %(self.name,self.age)
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

