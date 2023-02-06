import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
  
        
    def show(self):
        return self.x,self.y
    def __str__(self):
        return f'The coordinates of p1 are {self.x,self.y}'
      
    
    def move(self,x,y):
        self.x+=x
        self.y+y
    def __str__(self):
        return f'The move: {self.x,self.y}'
        pass
    def dist(self,x,y):
        self.d=((self.x**2)+(self.y**2))**0,5
    def __str__(self):
        return f'The distance:{self.d} '
    
p1=Point(int(input()),int(input()))

print(p1)
print(p1.move)
print(p1.show)

    
