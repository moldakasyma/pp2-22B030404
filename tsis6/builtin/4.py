import time
n=int(input())
sec=int(input())
m=n**0.5
time.sleep(sec/1000)
print("Square root of",n, "after",sec,"milliseconds is",m)
