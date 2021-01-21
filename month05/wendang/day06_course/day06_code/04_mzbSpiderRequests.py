"""
使用requests+lxml+xpath提取最新月份行政区划代码
"""
import re

import requests
from lxml import etree
from fake_useragent import UserAgent

class MzbSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.headers = {'User-Agent':UserAgent().random}

    def get_html(self, url):
        """请求功能函数"""
        html = requests.get(url=url, headers=self.headers).text

        return html

    def xfunc(self, html, x):
        """解析功能函数"""
        eobj = etree.HTML(html)
        r_list = eobj.xpath(x)

        return r_list

    def parse_html(self):
        """爬虫逻辑函数"""
        html = self.get_html(url=self.url)
        # 提取最新月份的href
        x = '//table/tr[1]/td[2]/a[@class="artitlelist"]/@href'
        href_list = self.xfunc(html, x)
        # href_list:['/article/sj/xzqh/2020/202101/20210100031547.shtml']
        if href_list:
            # two_url:假链接
            two_url = 'http://www.mca.gov.cn' + href_list[0]
            # 提取详情页的具体数据
            self.get_data(two_url)
        else:
            print('提取最新月份链接失败')

    def get_data(self, two_url):
        """提取具体数据(名称+编号)"""
        # two_html: 假的响应内容
        two_html = self.get_html(url=two_url)
        # 从假的two_html中提取真实返回数据的URL地址
        regex = 'window.location.href="(.*?)"'
        # real_url: 真实的链接
        real_url = re.findall(regex, two_html, re.S)[0]
        real_html = self.get_html(url=real_url)
        # 开始提取数据
        two_x = '//tr[@height=19]'
        # tr_list: [3210个tr节点对象]
        tr_list = self.xfunc(real_html, two_x)
        for tr in tr_list:
            item = {}
            item['code'] = tr.xpath('./td[2]/text() | ./td[2]/span/text()')[0].strip()
            item['name'] = tr.xpath('./td[3]/text()')[0].strip()
            print(item)

if __name__ == '__main__':
    spider = MzbSpider()
    spider.parse_html()
















