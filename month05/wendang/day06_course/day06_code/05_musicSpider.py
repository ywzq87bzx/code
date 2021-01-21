"""
selenium抓取网易云音乐top100歌曲信息
https://music.163.com/#/discover/toplist
"""
from selenium import webdriver

# 1.打开浏览器,输入URL地址
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get(url='https://music.163.com/#/discover/toplist')
# 2.切换iframe子页面
driver.switch_to.frame("contentFrame")
# 3.提取具体歌曲信息
tr_list = driver.find_elements_by_xpath("//table/tbody/tr")
for tr in tr_list:
    # 打印tr.text属性,发现竟然没有明显规律！！！
    # 此时我们应该依次提取每个字段数据
    item = {}
    item['rank'] = tr.find_element_by_xpath('.//span[@class="num"]').text
    item['title'] = tr.find_element_by_xpath('.//span[@class="txt"]/a/b').get_attribute('title').replace('\xa0', ' ')
    item['time'] = tr.find_element_by_xpath('.//span[@class="u-dur "]').text
    item['singer'] = tr.find_element_by_class_name("text").get_attribute('title')
    print(item)




























