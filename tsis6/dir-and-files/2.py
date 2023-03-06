import os
path=r"/Users/aja/Desktop/python/tsis6/dir-and-files/dd/all.txt"
f = open(path)
if os.path.exists(path):
    print("the path is exist!")
else:
    print("doesn't exist")
print(f.readable())
print(f.writable()) 
if os.access(path, os.X_OK):
    print("YES")
else:
    print("NO")