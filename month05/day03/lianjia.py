import requests
from lxml import etree
from fake_useragent import UserAgent


url='https://xa.lianjia.com/ershoufang/'
headers={'User-Agent':UserAgent().random}
html=requests.get(url=url,headers=headers)

eobj=etree.HTML(html)
li_list=eobj.xpath('//li[@class="clear LOGCLICKDATA"]')
for li in li_list:
    item={}
    name_list=li.xpath('//')