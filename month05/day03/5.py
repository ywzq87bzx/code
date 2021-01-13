import requests
from fake_useragent import UserAgent


path = 'http://wthrcdn.etouch.cn/weather_mini?city=蒲城县'
headers = {'User-Agent': UserAgent().random}
response= requests.get(path,headers=headers)
result = response.json()
print(result)