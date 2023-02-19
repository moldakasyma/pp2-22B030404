import datetime
x=datetime.datetime.now()
y=datetime.datetime.now().replace(microsecond=0)
print(x,y,sep="\n")