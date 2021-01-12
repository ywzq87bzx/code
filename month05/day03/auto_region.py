import json
import time
import requests
import re
from fake_useragent import UserAgent
# from urllib import response


# ---------获取定位---------
# info = requests.get('http://ipinfo.io/json').json()
# city=info['city']
# region=info['region']
# print(info,city,region)

# ---------根据主机IP获取定位-----
def search_region_by_ip(computer_ip):
    # url = 'http://xyq.163.com/news/index.html'
    # url ='https://www.ip138.com/iplookup.asp?ip=125.123.68.154&action=2'
    # 浙江省 嘉兴市
    # url ='https://www.ip138.com/iplookup.asp?ip=101.39.225.103&action=2'
    # 北京市 北京市
    # url ='https://www.ip138.com/iplookup.asp?ip=101.39.225.128&action=2'
    # 重庆市 重庆市
    url = 'https://www.ip138.com/iplookup.asp?ip=%s&action=2' % computer_ip
    headers = {'User-Agent': UserAgent().random}
    try:
        html = requests.get(url=url, headers=headers).content.decode('gb2312')
        # print(html)
        region = re.findall('ip_result = {"ASN归属地":".*?[省市](.*?)市\W', html, re.S)
        print(region)
        return region
    except Exception:
        print("Connection refused")
        # response.status_code = "Connection refused"


# -------根据地区得到天气---------
# url="http://www.webxml.com.cn//WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=57036"
# def get_weather(region):
def search_weather(region):
    url = "http://wthrcdn.etouch.cn/weather_mini?city=%s" % region
    response = requests.get(url=url)
    weather_data = json.loads(response.text)
    print(weather_data)
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    year = str(date).split("-")[0]
    month = str(date).split("-")[1]
    day = weather_data['data']['forecast'][0]['date']
    city = weather_data['data']['city']
    weather_high = weather_data['data']['forecast'][0]['high']
    print(year, month, day, city, weather_high)


# url = 'http://ip.42.pl/raw'
# computer_ip= requests.get(url).text
# computer_ip='125.123.68.154'
# computer_ip='101.39.225.103'
computer_ip='101.39.225.128'
region=search_region_by_ip(computer_ip)[0]
search_weather(region)
