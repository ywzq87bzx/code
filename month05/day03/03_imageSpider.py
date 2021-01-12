import requests
from fake_useragent import UserAgent
from lxml import etree
# url="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=961413237,3401260216&fm=26&gp=0.jpg"
url='https://tieba.baidu.com/p/7185877941'
headers = {'User-Agent': UserAgent().random}
html=requests.get(url=url,headers=headers).text
eobj=etree.HTML(html)
print(eobj)

src_list = eobj.xpath('//div[@class="video_src_wrapper"]/embed/@data-video')

print(src_list)
if src_list:
    video_url=src_list[0]
    video_html=requests.get(url=video_url,headers=headers).content
    with open("赵丽颖.mp4",'wb') as f:
        f.write(video_html)
else:
    print("视频提取失败")

# with open("林允儿.jpg",'wb') as f:
#     f.write(html)




