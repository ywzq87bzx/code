import datetime
import hashlib
import base64
import json
import requests  # 使用该库可以发送http/https请求


class YunTongXin():
    base_url = 'https://app.cloopen.com:8883'

    def __init__(self, accountSid, accountToken, appId, templateId):
        self.accountSid = accountSid
        self.accountToken = accountToken
        self.appId = appId
        self.templateId = templateId

    # 1 生成url:baseurl+业务url
    def get_request_url(self, sig):
        self.url = self.base_url + '/2013-12-26/Accounts/%s/SMS/TemplateSMS?sig=%s' % (self.accountSid, sig)
        return self.url
    def get_timestamp(self):
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        return now_str

    def get_sig(self, timestamp):
        s = self.accountSid + self.accountToken + timestamp
        md5 = hashlib.md5()
        md5.update(s.encode())
        return md5.hexdigest().upper()

    # 2构建请求包的包头
    def get_request_header(self, timestamp):
        s = self.accountSid + ':' + timestamp
        b_s = base64.b64encode(s.encode()).decode()
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': b_s
        }

    # 3 构造请求包的包体
    def get_request_body(self, phone, code):
        data = {
            'to': phone,
            'appId': self.appId,
            'templateId': self.templateId,
            'datas': [code, '3']
        }
        return data

    # 4 发送请求的方法
    def do_request(self, url, header, body):
        res = requests.post(url, headers=header,
                            data=json.dumps(body))
        return res.text

    # 5 将以上步骤串联
    def run(self, phone, code):
        # 1 构造url
        timestamp = self.get_timestamp()
        sig = self.get_sig(timestamp)
        url = self.get_request_url(sig)
        print(url)
        # 2 header
        header = self.get_request_header(timestamp)
        # 3 body
        body = self.get_request_body(phone, code)
        print(body)
        # 4 发送请求
        res = self.do_request(url, header, body)
        return res

if __name__ == '__main__':
    aid='8aaf0708762cb1cf0176b31065fd3148'
    token='b9044f29180b4c6794dc43334d96bc95'
    appid='8aaf0708762cb1cf0176b310666c314e'
    tid='1'
    x=YunTongXin(aid,token,appid,tid)
    res=x.run('18229093764','123456')
    print(res)