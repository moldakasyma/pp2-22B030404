def solve(numheads,numlegs):
    n='No solution'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
        
    return n,n
        
numheads=35
numlegs=94
print(solve(numheads,numlegs))
        