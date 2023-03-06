def multiple(mylist):
    ans=1
    for x in mylist:
        ans=ans*x
    return ans
mylist=list(map(int,input().split()))
print(multiple(mylist))
