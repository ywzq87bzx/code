# -*- coding: utf-8 -*-
import scrapy
from ..items import GuaziItem

class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    url = 'https://www.guazi.com/nc/buy/o{}/#bread'
    # 1.去掉start_urls变量
    # 2.重写start_requests()方法
    def start_requests(self):
        """生成所有要抓取的URL地址,一次性交给调度器入队列"""
        for o in range(1, 6):
            page_url = self.url.format(o)
            # scrapy.Request(): 交给调度器入队列
            # url参数: 交给调度器入队列的地址
            # callback参数: 最终返回的response找哪个函数解析
            yield scrapy.Request(url=page_url,
                                 callback=self.parse)

    # parse()被调用了5次,分别传了5页的response
    def parse(self, response):
        """一级页面解析函数"""
        x = '//ul[@class="carlist clearfix js-top"]/li'
        # li_list: [<selector1>,<selector2>,<selector3>,...]
        li_list = response.xpath(x)
        for li in li_list:
            # 想要：items.py中的GuaziItem类中的类变量赋值
            item = GuaziItem()
            item['href'] = 'https://www.guazi.com' + li.xpath('./a/@href').get()
            item['name'] = li.xpath('./a/@title').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()
            # 把详情页的链接item['href']继续交给调度器入队列
            # meta参数：不同的解析函数之间传递数据
            yield scrapy.Request(url=item['href'],
                                 meta={'item':item},
                                 callback=self.detail_page)

    # detail_page()被调用了200次,分别是每辆汽车的response
    def detail_page(self, response):
        """二级页面解析函数: 提取汽车里程、排量、变速箱"""
        # 接收item对象
        # meta会作为response的一个属性传递过来
        item = response.meta['item']
        item['km'] = response.xpath('//li[@class="two"]/span/text()').get()
        item['displace'] = response.xpath('//li[@class="three"]/span/text()').get()
        item['typ'] = response.xpath('//li[@class="last"]/span/text()').get()

        # 至此,一个汽车6个数据彻底提取完成,交给管道文件处理
        yield item















# yield语句：一个函数中一旦有了yield语句,这个函数当成生成器使用
# yield语句：可以让函数暂停再继续执行的语句
# 协程：微线程、纤程,比线程还要小的执行单元
       # yield语句就是实现协程关键字
       # 实现协程模块：greenlet、gevent ... ...











