import redis
# r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

#     大部分的方法的参数或返回值是字节串，不是字符串
#     encode()字符——字节串,decode()字节——字符
if __name__ == '__main__':


    # print(r.keys('*'))
    # r.flushdb()
    # r.set('username','aid2009班',ex=60)
    # print(r.get('username').decode())
    # r.incrby('fans',1000)
    # r.incr('fans')
    # print((r.get('fans')).decode())
    # r.lpush('task','1','2','3')
    # print(r.lrange('task',0,-1))
    # r.set('bk1','ab')
    # print(r.get('bk1'))
    # r.setbit('bk1',3,1)
    # print(r.get('bk1'))
    #
    # r.sadd('武将','张飞','赵云','周瑜')
    # r.sadd('文臣','诸葛亮','司马懿','郭嘉','周瑜')
    #
    # result=r.sinter('武将','文臣')
    # lst_all=[]
    # for r in result:
    #     lst_all.append(r.decode())
    # print(lst_all)

    # r.keys('*')
    # r.zadd('zk1',{'tedu':100})
    # r.zadd('zk1',{'tedu2':200})
    # print(r.zrange('zk1',0,-1,withscores=True))
    # r.zadd('zk2', {'tedu2': 300})
    # r.zadd('zk2', {'tedu3': 500})
    # print(r.zrange('zk2', 0, -1, withscores=True))
    # r.zunionstore('zk3',['zk1','zk2'],aggregate='sum')
    # print(r.zrange('zk3', 0, -1, withscores=True))
    # r.zunionstore('zk4', {'zk1':0.8, 'zk2':0.2}, aggregate='sum')
    # print(r.zrange('zk4', 0, -1, withscores=True))


    # 创建连接池并连接到redis
    pool = redis.ConnectionPool(password='123456')
    r = redis.Redis(connection_pool=pool)

    pipe = r.pipeline()
    pipe.set('fans', 50)
    pipe.incr('fans')
    pipe.incrby('fans', 100)
    pipe.execute()



