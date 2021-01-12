import pymongo
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent


class DoubanSpider:
    def __init__(self):
        self.url = 'https://book.douban.com/top250?start={}'
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['Doubanbook']
        self.myset = self.db['Doubanset']

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        self.parse_html(html)

    def parse_html(self, html):
        eobj = etree.HTML(html)
        table_list = eobj.xpath('//table')
        for table in table_list:
            item = {}
            item['title'] = table.xpath('.//div[@class="pl2"]/a/@title')[0].strip() if table.xpath('.//div[@class="pl2"]/a/@title') else None
            item['info'] = table.xpath('.//p[@class="pl"]/text()')[0].strip() if table.xpath('.//p[@class="pl"]/text()') else None
            item['score'] = table.xpath('.//span[@class="rating_nums"]/text()')[0].strip() if table.xpath('.//span[@class="rating_nums"]/text()') else None
            item['commit'] = table.xpath('.//span[@class="pl"]/text()')[0].strip().split('\n')[1].strip() if table.xpath('.//span[@class="pl"]/text()') else None
            item['comment'] = table.xpath('.//span[@class="inq"]/text()')[0].strip() if table.xpath('.//span[@class="inq"]/text()') else None
            print(item)
            self.myset.insert_one(item)

    def crawl(self):
        for i in range(10):
            start = i * 25
            page_url = self.url.format(start)
            self.get_html(url=page_url)
            time.sleep(random.uniform(0, 3))


if __name__ == '__main__':
    Douban = DoubanSpider()
    Douban.crawl()
