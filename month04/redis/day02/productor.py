import redis

r = redis.Redis(password='123456')
# 任务类型_发送者_接收者_内容
task = '%s_%s_%s_%s'%('sendMail','123@qq.com','456@qq.com','Hello World')
# 将任务放到消息队列[用列表来表示]中
r.lpush('pylt1',task)


