import re
import time

import requests
import random

class NovelSpider:
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'}

    def get_html(self,url):
        html = requests.get(url=url, headers=self.headers).text
        self.parse_html(html)
    def parse_html(self,html):
        reg='<div class="caption"><h4>.*?<a.*?title=.*?>(.*?)</a>.*?fs-12">(.*?)/(.*?)</small>.*?hidden-xs">(.*?)</p>'
        r_list=re.findall(reg,html,re.S)
        self.save_html(r_list)

    def save_html(self,r_list):
        for r_tuple in r_list:
            item={}
            # item['href']=r_tuple[0]
            item['title']=r_tuple[0].strip()
            item['author']=r_tuple[1].strip()
            item['comment']=r_tuple[3].strip()
            print(item)
    def crawl(self):
        for page in range(1,3):
            page_url=self.url.format(page)
            self.get_html(url=page_url)
            time.sleep(random.randint(1,2))

if __name__ == '__main__':
    spider = NovelSpider()
    spider.crawl()
