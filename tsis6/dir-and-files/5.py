mylist=list(map(int,input().split()))
with open('l.txt','w') as myfile:
    for x in mylist:
        myfile.write("%s\n"%x)

mytxt=open('l.txt')
print(mytxt.read) 