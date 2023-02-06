def spy_game(n):
    for i in range(0,len(n)):
        if n[i]==0:
            for j in range(i+1,len(n)):
                if n[j]==0:
                    for k in range (j+1,len(n)):
                        if n[k]==7:
                            return True
    return False
            
      
                        
   

l=list(map(int,input().split()))
print(spy_game(l))