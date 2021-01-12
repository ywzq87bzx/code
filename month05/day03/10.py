# -*- coding: utf-8 -*-
import re
from urllib import response
from fake_useragent import UserAgent
import requests




def search_region_by_ip(computer_ip):
# url = 'http://xyq.163.com/news/index.html'
# url ='https://www.ip138.com/iplookup.asp?ip=125.123.68.154&action=2'
# 浙江省 嘉兴市
# url ='https://www.ip138.com/iplookup.asp?ip=101.39.225.103&action=2'
# 北京市 北京市
# url ='https://www.ip138.com/iplookup.asp?ip=101.39.225.128&action=2'
# 重庆市 重庆市
    url = 'https://www.ip138.com/iplookup.asp?ip=%s&action=2'% computer_ip
    headers = {'User-Agent': UserAgent().random}
    try:
        html = requests.get(url=url,headers=headers).content.decode('gb2312')
        # print(html)
        region = re.findall('ip_result = {"ASN归属地":".*?[省市](.*?)市\W',html,re.S)
        # print(r_l)
        return region
    except Exception:
        response.status_code = "Connection refused"


