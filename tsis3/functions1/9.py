import math
def sphere_vol(r):
    return (4/3)*math.pi*r**3
r=int(input())
v=sphere_vol(r)
print(v)  