# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
"""
items.py - 定义要抓取的数据结构
"""
import scrapy

class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # 汽车链接、汽车名称、汽车价格、行驶里程、排量、变速箱
    href = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    km = scrapy.Field()
    displace = scrapy.Field()
    typ = scrapy.Field()








# 相当于：{'href':'', 'name':'', 'price':''}
# 定义了三个key,没有赋值
# 何时赋值？？爬虫文件将数据提取出来后给key赋值


