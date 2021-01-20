# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    url = 'https://maoyan.com/board/4?offset={}'
    # 重写start_requests()方法
    def start_requests(self):
        """生成所有要抓取的URL地址,交给调度器入队列"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            yield scrapy.Request(url=page_url, callback=self.get_film_data)

    def get_film_data(self, response):
        """解析提取数据"""
        dd_list = response.xpath('//dl/dd')
        for dd in dd_list:
            item = MaoyanItem()
            item['name'] = dd.xpath('.//p[@class="name"]/a/text()').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()

            # 至此,一条完整的数据提取完成,交给项目管道处理
            yield item
