from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://mail.163.com/')

# 切换iframe
node = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
driver.switch_to.frame(node)
# 用户名、密码、登录按钮节点
driver.find_element_by_name("email").send_keys("wangweichao_2020")
driver.find_element_by_name("password").send_keys("zhanshen001")
driver.find_element_by_id("dologin").click()






















