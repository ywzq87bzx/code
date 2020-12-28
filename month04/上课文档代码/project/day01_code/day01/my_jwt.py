import json
import base64
import time
import hmac
import copy


class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def encode(payload, key, exp=300):
        # 生成json web token
        # 1 header
        header = {'alg': 'HS256', 'typ': 'JWT'}
        # 1.1 先把对象序列化为字符串
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        # print(header_json)
        # 1.2 把字符串encode为字节串，再进行base64编码
        header_bs = Jwt.b64encode(header_json.encode())
        print(header_bs)
        # 2 payload
        payload_data = copy.deepcopy(payload)
        # 在私有声明的基础上，增加一个公有声明（token的过期时间）
        payload_data['exp'] = time.time() + int(exp)
        # 将payload序列化为字符串
        payload_json = json.dumps(payload_data, separators=(',', ':'), sort_keys=True)
        # print(payload_json)
        # 将字符串转字节串，再base64编码
        payload_bs = Jwt.b64encode(payload_json.encode())
        print(payload_bs)
        # 3 sign（消息认证码）
        hm = hmac.new(key.encode(),
                      header_bs + b'.' + payload_bs,
                      digestmod='SHA256')
        # 返回值本身就是字节串
        digest = hm.digest()
        hm_bs = Jwt.b64encode(digest)
        token = header_bs + b'.' + payload_bs + b'.' + hm_bs
        return token

    # 去除=
    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')

    @staticmethod
    def b64decode(b_s):
        rem = len(b_s) % 4
        if rem > 0:
            b_s += b'=' * (4 - rem)
        # 补完 = 后解码
        return base64.urlsafe_b64decode(b_s)


    @staticmethod
    def decode(token, key):
        header_bs, payload_bs, sign = token.split(b'.')
        hm = hmac.new(key.encode(),
                      header_bs + b'.' + payload_bs,
                      digestmod='SHA256')
        # 返回值本身就是字节串
        digest = hm.digest()
        if Jwt.b64encode(digest) != sign:
            raise
        # 从payload中获取公有声明和私有声明
        # 补完=后，再解码
        payload_js = Jwt.b64decode(payload_bs)
        # 将字符串反序列化为对象
        payload = json.loads(payload_js)
        exp = payload['exp']
        now = time.time()
        if now > exp:
            raise
        return payload


if __name__ == '__main__':
    token = Jwt.encode({'username': 'tedu'}, '123456',3)
    print(token)
    time.sleep(4)
    print(Jwt.decode(token, '123456'))
