import re
import time

import requests
import random

# https://maoyan.com/board/4?offset=0
# https://maoyan.com/board/4?offset=10
# https://maoyan.com/board/4?offset=20

class MovieSpider:

    def __init__(self):
        self.url='https://maoyan.com/board/4?offset={}'
        self.headers={'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'}

    def get_html(self,url):
        html=requests.get(url=url,headers=self.headers).text
        self.parse_html(html)

    def parse_html(self,html):
        reg='<div class="movie-item-info">.*?data-act="boarditem-click" data-val=.*?>(.*?)</a></p>.*?<p class="star">(.*?)</p>.*?上映时间：(.*?)</p>'
        r_list=re.findall(reg,html,re.S)
        self.save_html(r_list)

    def save_html(self,r_list):
        item = {}
        for r_tuple in r_list:
            item['电影名称'] = r_tuple[0].strip()
            item['电影主演'] = r_tuple[1].strip()
            item['上映时间'] = r_tuple[2].strip()
            print(item)

    def crawl(self):
        # 爬取榜单前几页
        start=int(input("请输入起始页："))
        end=int(input("请输入终止页："))
        for page in range(start,end+1):
            page_url=self.url.format((page-1)*10)
            print(page)
            self.get_html(url=page_url)
            time.sleep(random.randint(1, 5))

if __name__ == '__main__':
    Movie=MovieSpider()
    Movie.crawl()




