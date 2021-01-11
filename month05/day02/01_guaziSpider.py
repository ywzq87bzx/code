"""
一级页面: 汽车详情页链接
二级页面: 汽车名称、... ...
增量爬虫
"""
import requests
import re
import time
import random
from hashlib import md5
import redis
import sys

class CarSpider:
    def __init__(self):
        self.url = 'https://www.guazi.com/bj/buy/o{}/#bread'
        self.headers = {
            'Cookie':'antipas=9c07029166N5NdB61090hVK; uuid=80480517-5cc9-4687-dd22-1df01a0fd096; ganji_uuid=1561931600173065002669; lg=1; clueSourceCode=%2A%2300; sessionid=6a15cce4-fb19-4d7e-a6e6-1a5b566e6a51; Hm_lvt_bf3ee5b290ce731c7a4ce7a617256354=1609990529,1610272931,1610328303; lng_lat=116.91886_39.95641; gps_type=1; close_finance_popup=2021-01-11; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2280480517-5cc9-4687-dd22-1df01a0fd096%22%2C%22ca_city%22%3A%22langfang%22%2C%22sessionid%22%3A%226a15cce4-fb19-4d7e-a6e6-1a5b566e6a51%22%7D; user_city_id=12; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A33980038794%7D; preTime=%7B%22last%22%3A1610328485%2C%22this%22%3A1609990531%2C%22pre%22%3A1609990531%7D; Hm_lpvt_bf3ee5b290ce731c7a4ce7a617256354=1610328484; cityDomain=zz',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        }
        # 连接redis做增量
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def get_html(self, url):
        """请求功能函数"""
        html = requests.get(url=url, headers=self.headers).content.decode('utf-8')

        return html

    def refunc(self, regex, html):
        """解析功能函数"""
        r_list = re.findall(regex, html, re.S)

        return r_list

    def md5_href(self, href):
        """md5加密功能函数"""
        m = md5()
        m.update(href.encode())

        return m.hexdigest()

    def parse_html(self, url):
        """爬虫逻辑函数由此开始啦~~~"""
        first_html = self.get_html(url=url)
        first_regex = '<li data-scroll-track=.*?href="(.*?)"'
        # href_list: ['', '', '', ...]
        href_list = self.refunc(first_regex, first_html)
        # for循环遍历,提取每辆汽车的具体数据
        for href in href_list:
            # 做增量判断
            finger = self.md5_href(href)
            if self.r.sadd('car:spider', finger) == 1:
                # detail_page():抓取1辆汽车的具体数据
                self.detail_page(href)
                # 控制频率
                time.sleep(random.randint(0, 1))
            else:
                sys.exit('更新完成')

    def detail_page(self, href):
        """二级页面解析：提取1辆汽车的具体数据"""
        second_url = 'https://www.guazi.com' + href
        second_html = self.get_html(url=second_url)
        second_regex = '<div class="product-textbox">.*?<h1 class="titlebox">(.*?)</h1>.*?<li class="two"><span>(.*?)</span>.*?<li class="three"><span>(.*?)</span>.*?<li class="last"><span>(.*?)</span>.*?<span class="price-num">(.*?)</span>'
        car_info_list = self.refunc(second_regex, second_html)
        # car_info_list: [('名称','里程','排量','变速箱','价格')]
        if car_info_list:
            item = {}
            item['title'] = car_info_list[0][0].strip().split('\r\n')[0]
            item['km'] = car_info_list[0][1].strip()
            item['displace'] = car_info_list[0][2].strip()
            item['type'] = car_info_list[0][3].strip()
            item['price'] = car_info_list[0][4].strip()
            print(item)
        else:
            print('汽车具体信息提取失败')

    def crawl(self):
        for page in range(1, 2):
            page_url = self.url.format(page)
            self.parse_html(url=page_url)
            # 控制频率
            time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    spider = CarSpider()
    spider.crawl()

































