import re

import requests



# resp=requests.get(url="https://www.jd.com/")
# html=resp.text
# html=resp.content
# print(html)


# resp=requests.get(url="http://httpbin.org/get",
#                   headers={'User-Agent':'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'})
# html=resp.text
#
# print(html)

# url='https://www.guazi.com/xa/buy/{}/#bread'
# for i in range(1,21):
#     result=url.format(i)
#     print(result)

word=input('请输入搜索关键字：')
url='http://www.baidu.com/s?wd={}'.format(word)
headers ={'User-Agent':'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'}
html=requests.get(url=url,headers=headers).text
filename="{}.html".format(word)
with open(filename,'w',encoding='utf-8') as f:
    f.write(html)


