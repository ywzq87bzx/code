import csv
with open('test.csv','w',newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['超哥哥','25'])

f=open('test.csv','a',newline='')
writer = csv.writer(f)
writer.writerow(['白哥哥','27'])
f.close()