class IOString():
    def __init__(self):
        self.str1 = ""

    def getString(self):
        self.str1 = input()

    def printString(self):
        print(self.str1.upper())

str1 = IOString()
str1.getString()
str1.printString()
