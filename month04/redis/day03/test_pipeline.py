
import redis
import time

pool = redis.ConnectionPool(password='123456')
r = redis.Redis(connection_pool=pool)

def withpipeline(r):
    p = r.pipeline()
    for i in range(1000):
        key = 'test1' + str(i)
        value = i+1
        p.set(key, value)
    p.execute()

def withoutpipeline(r):
    for i in range(1000):
        key = 'test2' + str(i)
        value = i+1
        r.set(key, value)

if __name__ == '__main__':

 i=0
 a=0
 while i<20:
    t1=time.time()
    withpipeline(r)
    # withoutpipeline(r)    0.0568
    t2=time.time()
    t=t2-t1
    a+=t
    i=i+1
    print('time is %s' % t)
a1=a/20
print('time is %s' % a1 )
