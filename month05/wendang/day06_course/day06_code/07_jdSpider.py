"""
selenium执行js脚本
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(url='https://search.jd.com/Search?keyword=%E9%92%B1&enc=utf-8&pvid=83b95124eb7a4079a3a3bd0c28394f94')
# 滚动: 执行JS脚本
driver.execute_script(
    'window.scrollTo(0,document.body.scrollHeight)'
)
# 休眠：给页面元素加载预留时间
time.sleep(2)
# 提取数据
li_list = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
print(len(li_list))































