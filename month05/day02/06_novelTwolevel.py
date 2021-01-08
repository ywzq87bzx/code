import sys
import time

import pymysql
import requests
import random
import re
import redis
import hashlib
from fake_useragent import UserAgent


class NovelSpider1:
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        # self.db = pymysql.connect('localhost', 'root', '123456', 'noveldb2', charset='utf8')
        # self.cur = self.db.cursor()
        self.r = redis.Redis(host='127.0.0.1',port=6379,db=0)


    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url,
                            headers=headers).text
        return html

    def func_html(self, regex, html):
        r_list = re.findall(regex, html, re.S)
        return r_list

    def md5_href(self,href):
        md5 = hashlib.md5()
        md5.update(href.encode())
        result = md5.hexdigest()
        return result

    def parse_html(self, url):
        first_html = self.get_html(url=url)
        first_regex = '<div class="caption">.*?<a href="(.*?)" title="(.*?)">.*?<small.*?>(.*?)</small>.*?>(.*?)</p>'
        first_list = self.func_html(first_regex, first_html)
        for first in first_list:
            item = {}
            item['href'] = first[0]
            item['title'] = first[1]
            item['author'] = first[2]
            item['comment'] = first[3]
            # 接着抓取二级页面的数据(item['herf'])
            finger=self.md5_href(item['href'])
            if self.r.sadd('novel:spider',finger):
                self.parse_two_page(item)
            else:
                sys.exit("更新完成")

    def parse_two_page(self, item):
        second_html = self.get_html(url=item['href'])
        second_regex = '<dd class="col-md-4"><a href="(.*?)">(.*?)</a></dd>'
        second_list = self.func_html(second_regex, second_html)
        item['novel_info'] = second_list
        # self.save_html(item)


    def save_html(self,item):
        ins = 'insert into novel_tab values(%s,%s,%s,%s,%s)'
        # self.cur.execute(ins, item)
        # self.db.commit()


    def crawl_html(self):
        for page in range(1, 3):
            page_url = self.url.format(page)
            self.parse_html(url=page_url)
            time.sleep(random.randint(1, 5))
        # self.cur.close()
        # self.db.close()

if __name__ == '__main__':
    spider = NovelSpider1()
    spider.crawl_html()
