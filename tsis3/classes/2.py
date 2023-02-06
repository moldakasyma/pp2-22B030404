class Shape():
    def __init__(self):
        pass

    def area(self):
        print(0)

class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length*self.length

asqr = Square(int(input()))
print(asqr.area())   
print(Shape.area())   

 