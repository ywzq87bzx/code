# 1. 简单的爬虫:
from urllib.request import urlopen




url = "http://ip-api.com/json/110.84.0.129"
urlObj = urlopen(url)

# 服务端返回的页面信息, 此处为字符串类型
pageContent = urlObj.read().decode('utf-8')
print(pageContent)
print(type(pageContent))

# 2. 处理Json数据
import json
# 解码: 将json数据格式解码为python可以识别的对象;
dict_data = json.loads(pageContent)
print(dict_data)
print(type(dict_data))

print("""
所在城市: %s
所在国家: %s

""" %(dict_data['city'], dict_data['country']))