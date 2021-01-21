# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        """解析提取数据: 提取 百度一下,你就知道"""
        # xpath(): [<selector xpath='' data=''>]
        # extract(): ['百度一下,你就知道']
        # extract_first(): '百度一下,你就知道'
        # get(): '百度一下,你就知道' 等价于 extract_first()
        result = response.xpath('/html/head/title/text()')
        print(result.extract())
        print(result.extract_first())
        print(result.get())




