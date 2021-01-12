from urllib.request import urlopen
from json import load


import re
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException


def Searchip(ip):
    print(ip)
    # url = 'https://ip.cn/?ip=' + ip
    # url = 'http://m.ip138.com/ip.asp?ip=' + ip
    url = 'http://freegeoip.net/json/%s' %(ip)
    print(url)

    # 请求头
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',

        # 'Referer': '',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, '
                      'like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 '
    }

    try:
        # 写入User Agent信息
        response = requests.get(url, headers=header)
        # 读取响应信息并解码
        if response.status_code == 200:
            htmlcode = response.text
            print(htmlcode)
    except ReadTimeout:
        print('ReadTimeout')
    except HTTPError:
        print('HTTPError')
    except RequestException:
        print('RequestException error')

    data_re = re.compile('所在地理位置：<code>(.*?)</code>', re.S)
    try:
        EquipmentDepot = data_re.findall(htmlcode)
        print(EquipmentDepot[0])
    except:
        print('RE Error')


my_ip = urlopen('http://ip.42.pl/raw').read()
print('ip.42.pl', my_ip.decode())
Searchip(my_ip.decode())