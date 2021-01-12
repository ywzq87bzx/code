import re
import time

import csv
import requests
import random

class NovelSpider:
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'}
        self.f =open('novel.csv','w')
        self.writer = csv.writer(self.f)
    def get_html(self,url):
        html = requests.get(url=url, headers=self.headers).text
        self.parse_html(html)
    def parse_html(self,html):
        reg='<div class="caption">.*?<a href="(.*?)" title="(.*?)">.*?<small.*?>(.*?)</small>.*?>(.*?)</p>'
        r_list=re.findall(reg,html,re.S)
        self.save_html(r_list)

    def save_html(self,r_list):
            for r_tuple in r_list:
                self.writer.writerow(r_tuple)
                print(r_tuple)
    def crawl(self):
        for page in range(1,3):
            page_url=self.url.format(page)
            self.get_html(url=page_url)
            time.sleep(random.randint(1,2))
        self.f.close()

if __name__ == '__main__':
    spider = NovelSpider()
    spider.crawl()