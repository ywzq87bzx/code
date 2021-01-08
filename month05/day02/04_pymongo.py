import pymongo

conn=pymongo.MongoClient('localhost',27017)
db=conn['studb']
myset=db['stuset']
myset.insert_one({'title':'花千骨', 'actor':'美丽的赵丽颖'})
