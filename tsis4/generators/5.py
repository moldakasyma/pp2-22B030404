def down(n):
    i=n
    while i>0:
        yield i
        i-=1    
        if i==0:
            break
        
        
for i in down(int(input())):
    print(i)