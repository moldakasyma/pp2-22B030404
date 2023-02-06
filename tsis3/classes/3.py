class Shape():
    def __init__(self):
        pass

    def area(self):
        print(0)
class Rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width


arectangle=Rectangle(3,4)
print(arectangle.area())
