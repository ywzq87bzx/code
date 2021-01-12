import json
import time
import requests

# info = requests.get('http://ipinfo.io/json').json()
# city=info['city']
# region=info['region']
# print(info,city,region)


# url="http://www.webxml.com.cn//WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=57036"
# def get_weather(region):
url="http://wthrcdn.etouch.cn/weather_mini?city=嘉兴"
response=requests.get(url=url)
weather_data=json.loads(response.text)
print(weather_data)
date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
year = str(date).split("-")[0]
month = str(date).split("-")[1]
day = weather_data['data']['forecast'][0]['date']
city = weather_data['data']['city']
weather_high = weather_data['data']['forecast'][0]['high']
print(year,month,day,city,weather_high)



