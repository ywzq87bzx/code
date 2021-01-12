import json

import requests
# requests.adapters.DEFAULT_RETRIES = 10
# from bs4 import BeautifulSoup


# def get_address(ip):
# url = "http://ip138.com/ips138.asp"
url ='http://ip.taobao.com/service/getIpInfo.php?ip='
# url ='http://www.ip.cn/101.39.225.103'
kw2 = {'ip': '101.39.225.103'}
# r = requests.request('GET', url, params=kw2)

r = requests.get(url=url, params=kw2)


print(r.json())
r.encoding = 'gbk'
demo = r.text
print(demo)
    # soup = BeautifulSoup(demo, "html.parser")
    # soup = soup.ul
    # address = soup.contents[0].string[5:]
    # address = address.split(' ')[0]
    # return address