"""
selenium操作鼠标三步走：
1、实例化鼠标事件类对象
2、为鼠标指定行为
3、执行鼠标行为
"""
import time

from selenium import webdriver
# 导入鼠标事件类
from selenium.webdriver import ActionChains

# 1.打开浏览器,输入百度URL地址
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url='http://www.baidu.com/')
# 2.鼠标移动到右上角 设置 节点
node = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
# 实例化、指定行为、执行行为
ActionChains(driver).move_to_element(node).perform()
# 3.找到 高级搜索 节点,并点击
time.sleep(1)
driver.find_element_by_link_text('高级搜索').click()



























