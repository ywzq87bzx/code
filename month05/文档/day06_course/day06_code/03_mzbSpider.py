"""
selenium抓取民政部最新行政区划代码数据
"""
from selenium import webdriver
import time
import redis
from hashlib import md5
import sys

class MzbSpider:
    def __init__(self):
        # 设置无界面
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)

        self.driver.get(url='http://www.mca.gov.cn/article/sj/xzqh/2020/')
        # 连接redis数据库
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def md5_href(self, href):
        """md5加密功能函数"""
        m = md5()
        m.update(href.encode())

        return m.hexdigest()

    def parse_html(self):
        """爬虫逻辑函数"""
        newest_node = self.driver.find_element_by_xpath('//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[1]/td[2]/a')
        href = newest_node.get_attribute('href')
        finger = self.md5_href(href)
        # 返回值1: 说明之前没抓过,是新更新的月份
        if self.r.sadd('mzb:spiders', finger) == 1:
            newest_node.click()
            # 最好休眠一下,给页面元素的加载预留时间
            time.sleep(1)
            # 切换句柄,li: [<handle1>, <handle2>]
            li = self.driver.window_handles
            self.driver.switch_to.window(li[1])
            # 开始提取数据
            tr_list = self.driver.find_elements_by_xpath('//tr[@height="19"]')
            for tr in tr_list:
                info_list = tr.text.split()
                item = {}
                item['code'] = info_list[0].strip()
                item['name'] = info_list[1].strip()
                print(item)
        else:
            sys.exit('结束!!!')

if __name__ == '__main__':
    spider = MzbSpider()
    spider.parse_html()
























