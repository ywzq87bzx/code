from celery import Celery

#1 创建Celery对象
app=Celery('adi2009',broker='redis://@127.0.0.1:6379/1')


#2 创建任务函数
@app.task
def task_test():
    print("task is running....")