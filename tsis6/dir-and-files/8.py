import os
file_path=os.path.abspath(input())
try:
    os.remove(file_path)
except:
    print("No such a file")