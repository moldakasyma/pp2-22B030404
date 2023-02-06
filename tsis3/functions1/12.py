def histogram(n):
    for i in n:
        output = ''
        times = i
        while( times > 0 ):
          output += '*'
          times -=1
        print(output)
        
histogram(list(map(int,input().split())))


