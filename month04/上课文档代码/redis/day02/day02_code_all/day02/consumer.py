import redis
r = redis.Redis(password='123456')

while True:
    # 1 从队列中取出任务
    task = r.brpop('pylt1',5)
    # (b'pylt1', b'sendMail_123@qq.com_456@qq.com_Hello World')
    print(task)
    if task:
        # 有任务，执行任务
        task_data =task[1]
        task_str = task_data.decode()
        task_list = task_str.split('_')
        print('-receive task,task is %s-'%task_list[0])
        if task_list[0] == 'sendMail':
            print('call send mail function')
    else:
        print('-no task!-')