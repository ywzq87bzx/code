import pymysql

db = pymysql.connect(
    'localhost', 'root', '123456', 'noveldb', charset='utf8'
)

cursor = db.cursor()

ins = 'insert into novel_tab values(%s,%s,%s,%s)'
novel_li = ['花千骨', 'http://zly.com', '赵丽颖', '小骨的传奇一生']
cursor.execute(ins, novel_li)

db.commit()
cursor.close()
db.close()
