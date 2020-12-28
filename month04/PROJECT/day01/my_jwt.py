import json
import base64
import time
import hmac
import copy


class Jwt():
    def __init__(self):
        pass
    @staticmethod
    def encode(payload,key,exp=300):
        # 生成json_web_token
        # 1 header
        header={'alg':'HS256', 'typ':'JWT'}
        # 先把对象序列化为字符串
        header_json=json.dumps(header,separators=(',',':'),sort_keys=True)
        print(header_json)
        header_bs=Jwt.b64encode(header_json.encode())
        print(header_bs)
        # 2 payload
        payload_data=copy.deepcopy(payload)
        payload_data['exp']=time.time()+int(exp)
        payload_json=json.dumps(payload_data,separators=(',',':'),sort_keys=True)
        print(payload_json)
        payload_bs=Jwt.b64encode(payload_json.encode())
        print(payload_bs)
        # 3 sign(消息认证码）
        hm=hmac.new(key.encode(),
                    header_bs+b'.'+payload_bs,
                    digestmod='SHA256'
                    )
        digest=hm.digest()
        print(digest)
        hm_bs=Jwt.b64encode(digest)
        token=header_bs+b'.'+payload_bs+b'.'+hm_bs
        return token

    @staticmethod
    def b64decode(b_s):
        rem=len(b_s)%4
        if rem>0:
            b_s+=b'='*(4-rem)
            return base64.urlsafe_b64decode(b_s)


    @staticmethod
    def b64encode(j_s):
        return  base64.urlsafe_b64encode(j_s).replace(b'=',b'')
    @staticmethod
    def decode(token,key):
        header_bs,payload_bs,sign=token.split(b'.')
        hm=hmac.new(key.encode(),
                    header_bs + b'.' + payload_bs,
                    digestmod='SHA256'
                    )
        digest=hm.digest()
        if Jwt.b64encode(digest)!=sign:
            raise
        payload_js=Jwt.b64decode(payload_bs)
        payload=json.loads(payload_js)
        exp=payload['exp']
        now=time.time()
        if now>exp:
            raise
        return payload



if __name__ == '__main__':
    token=Jwt.encode({'username':'tedu'},'123456')
    print(token)
    # time.sleep(60)
    print(Jwt.decode(token, '123456'))