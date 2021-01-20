from selenium import webdriver

# 设置无头(无界面)模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get(url='https://maoyan.com/board/4')

def get_one_page():
    x = '//*[@id="app"]/div/div/div[1]/dl/dd'
    dd_list = driver.find_elements_by_xpath(x)
    for dd in dd_list:
        # text属性：获取当前节点及子节点和后代节点文本内容
        # info_list: ['1','活着','牛犇','1995','9.6']
        info_list = dd.text.split('\n')
        item = {}
        item['rank'] = info_list[0]
        item['title'] = info_list[1]
        item['star'] = info_list[2]
        item['time'] = info_list[3]
        item['score'] = info_list[4]
        print(item)

while True:
    get_one_page()
    try:
        # selenium当无法定位到节点时,会抛出异常NoSuchElement
        driver.find_element_by_link_text('下一页').click()
    except Exception as e:
        print('恭喜你,抓取完成,你真棒~~~')
        driver.quit()
        break





















