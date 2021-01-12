import requests



path = 'http://wthrcdn.etouch.cn/weather_mini?city=蒲城县'
response= requests.get(path)
result = response.json()
print(result)