

# import requests
# from fake_useragent import UserAgent
# from lxml import etree
#
#
#
#
#
# url='https://www.ip138.com/iplookup.asp?ip=101.39.225.103&action=2'
# headers = {'User-Agent': UserAgent().random}
# html=requests.get(url=url,headers=headers)
# html=html.unicode("gb2312").encode("utf8")
#
# print(i)


import requests


def checkip(ip):
    URL = 'https://www.ip138.com/iplookup.asp?ip=101.39.225.103&action=2'
    try:
        # r = requests.get(URL, params=ip, timeout=3)
        r = requests.get(URL,timeout=3)
    except requests.RequestException as e:
        print(e)
    else:
        json_data = r.json()
        if json_data[u'code'] == 0:
            print ('所在国家： ' + json_data[u'data'][u'country'].encode('utf-8'))
            print  ('所在地区： ' + json_data[u'data'][u'area'].encode('utf-8'))
            print('所在省份： ' + json_data[u'data'][u'region'].encode('utf-8'))
            print('所在城市： ' + json_data[u'data'][u'city'].encode('utf-8'))
            print('所属运营商：' + json_data[u'data'][u'isp'].encode('utf-8'))
        else:
            print('查询失败,请稍后再试！')


ip = {'ip': '202.102.193.68'}
checkip(ip)