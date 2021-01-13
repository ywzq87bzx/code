import requests
import json
import time
import random
from fake_useragent import UserAgent
import re

class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        return html

    def get_total(self):
        total_url = 'https://movie.douban.com/j/chart/top_list_count?type=11&interval_id=100%3A90'
        total_html = json.loads(self.get_html(url=total_url))
        return total_html['total']

    def parse_html(self, url):
        html = json.loads(self.get_html(url=url))
        for one_film_dict in html:
            item = {}
            item['rank'] = one_film_dict['rank']
            item['name'] = one_film_dict['title']
            item['time'] = one_film_dict['release_date']
            item['score'] = one_film_dict['score']
            print(item)
    def crawl(self):
        total = self.get_total()
        for start in range(0,total,20):
            page_url = self.url.format(start)
            self.parse_html(url=page_url)
            time.sleep(random.randint(0,1))

if __name__ == '__main__':
    Douban=DoubanSpider()
    Douban.crawl()
