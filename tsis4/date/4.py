from datetime import datetime,time
x=datetime.now()
y=datetime.strptime('2020-02-20 02:02:02','%Y-%m-%d %H:%M:%S')
z=(x-y).seconds
print(z)
