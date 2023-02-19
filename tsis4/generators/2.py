def even(n):
    i=0
    while i<n:
        
            yield i
            i+=2
for i in even(int(input())):
    print(i,end=',')

        