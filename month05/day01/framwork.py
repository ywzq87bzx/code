import random

import requests
import time

class TiebaSpider:
    def __init__(self):
        self.url='http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers={'User-Agent':'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'}

    def get_html(self,url):
        html=requests.get(url=url,headers=self.headers).text
        return html
    def parse_html(self):
        pass
    def save_html(self,filename,html):
        with open(filename,'w',encoding='utf-8') as f:
            f.write(html)

    def crawl(self):
        name=input("请输入贴吧名：")
        start=int(input("请输入起始页："))
        end=int(input("请输入终止页："))
        for page in range(start,end+1):
            pn=(page-1)*50
            page_url=self.url.format(name,pn)
            html=self.get_html(url=page_url)
            filename='%s_第%s页.html'%(name,page)
            self.save_html(filename,html)
            time.sleep(random.randint(1,2))
            print('%d页抓取完成'%page)


if __name__ == '__main__':
    spider=TiebaSpider()
    spider.crawl()
