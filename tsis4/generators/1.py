def gen(n):
    i=0
    while i<n:
        yield i**2
        i+=1
        
for i in gen(int(input())):
    print(i)

