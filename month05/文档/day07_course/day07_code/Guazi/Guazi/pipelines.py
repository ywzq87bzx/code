# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道1 - 终端打印输出汽车名字
class GuaziPipeline(object):
    def process_item(self, item, spider):
        # 打印测试
        print(item['name'])
        return item

# 管道2 - 持久化到MySQL
import pymysql
class GuaziMysqlPipeline(object):
    def open_spider(self, spider):
        """爬虫项目启动时,只执行1次,一般用于数据库连接"""
        self.db = pymysql.connect(
            'localhost', 'root', '123456', 'cardb', charset='utf8'
        )
        self.cur = self.db.cursor()
        self.ins = 'insert into cartab values(%s,%s,%s)'

    def process_item(self, item, spider):
        li = [
            item['name'],
            item['price'],
            item['href']
        ]
        self.cur.execute(self.ins, li)
        self.db.commit()

        return item

    def close_spider(self, spider):
        """爬虫项目结束时,只执行1次,一般用于数据库的断开"""
        self.cur.close()
        self.db.close()

# 管道3 - 持久化到MongoDB数据库
import pymongo
class GuaziMongoPipeline(object):
    def open_spider(self, spider):
        """连接mongodb数据库"""
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['cardb']
        self.myset = self.db['carset']

    def process_item(self, item, spider):
        self.myset.insert_one(dict(item))

        return item

# mongodb命令行确认
# mongo
# use cardb
# db.carset.count()





