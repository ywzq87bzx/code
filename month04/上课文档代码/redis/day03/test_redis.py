import redis

r = redis.Redis()

if __name__ == '__main__':
    # 大部分的方法的参数或返回值是字节串，不是字符串
    # 字符串->字节串：encode()
    # 字节串->字符串: decode()
    print(r.keys('*'))
    # 清一下库(学习环境中)
    r.flushdb()
    # 1 string
    r.set('username', 'aid2009班', ex=60)
    print(r.get('username').decode())
    r.incrby('fans', 1000)
    r.incr('fans')
    print(r.get('fans'))
    # 2 list
    r.lpush('tasks', 't1', 't2', 't3', 't4', 't5')
    print(r.lrange('tasks', 0, -1))
    r.rpop('tasks')
    print(r.lrange('tasks', 0, -1))
    # 3 bitmap（属于字符串类型）
    r.set('bk1', 'ab')
    print(r.get('bk1'))
    r.setbit('bk1', 3, 1)
    print(r.get('bk1'))
    # 4 hash
    r.hset('p2', 'name', 'lisi')
    r.hmset('p2', {'age': 18, 'address': 'beijing'})
    print(r.hget('p2', 'name'))
    print(r.hgetall('p2'))
    # 5 set
    r.sadd('武将', '张飞', '赵云', '周瑜')
    r.sadd('文臣', '诸葛亮', '司马懿', '郭嘉', '周瑜')
    # 输出:【10分钟】
    result = r.sinter('武将', '文臣')
    result = r.sunion('武将', '文臣')
    print(result)
    lst_all = []
    for res in result:
        lst_all.append(res.decode())
    print(lst_all)

    # 有序集合
    r.zadd('zk1', {'tedu': 100})
    r.zadd('zk1', {'tedu2': 200})
    print(r.zrange('zk1', 0, -1, withscores=True))
    r.zadd('zk2', {'tedu2': 300})
    r.zadd('zk2', {'tedu3': 500})
    print(r.zrange('zk2', 0, -1, withscores=True))

    # 不带权重的
    r.zunionstore('zk3', ['zk1', 'zk2'], aggregate='sum')
    print(r.zrange('zk3', 0, -1, withscores=True))
    # 带权重的
    r.zunionstore('zk4', {'zk1': 0.8, 'zk2': 0.2}, aggregate='sum')
    print(r.zrange('zk4', 0, -1, withscores=True))
