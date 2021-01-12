import requests
import json
import time
import random
from hashlib import md5

class YdSpider:
    def __init__(self):
        self.url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "246",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=1325636116@10.108.160.100; JSESSIONID=aaa5wjDr-bxfg5i5bw1Bx; OUTFOX_SEARCH_USER_ID_NCOO=543944615.7905612; ___rl__test__cookies=1610440265773",
            "Host": "fanyi.youdao.com",
            "Origin": "http//fanyi.youdao.com",
            "Referer": "http//fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        self.word=input("请输入要翻译的单词:")
    def md5s(self,s):
        m=md5()
        m.update(s.encode())
        sign = m.hexdigest()
        return sign
    def get_ts_salt_sign(self):
        ts=str(int(time.time()*1000))
        salt=ts+str(random.randint(0,9))
        string1="fanyideskweb" + self.word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        sign=self.md5s(string1)
        return ts,salt,sign
    def attack_yd(self):
        ts,salt,sign=self.get_ts_salt_sign()
        # print(ts,salt,sign)
        data={
            "i":self.word,
            "from":"AUTO",
            "to":"AUTO",
            "smartresult":"dict",
            "client":"fanyideskweb",
            "salt":salt,
            "sign":sign,
            "lts":ts,
            "bv":"34f593a29e1453bc91be38672003da85",
            "doctype":"json",
            "version":"2.1",
            "keyfrom":"fanyi.web",
            "action":"FY_BY_REALTlME",
        }
        html=requests.post(url=self.url,
                           data=data,
                           headers=self.headers).json()
        # print(html)
        result = html['translateResult'][0][0]['tgt']
        print(result)


if __name__ == '__main__':
    spider=YdSpider()
    spider.attack_yd()

