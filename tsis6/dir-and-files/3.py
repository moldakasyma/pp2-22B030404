import os
path = "/Users/aja/Desktop/python/tsis6/builtin"
if os.path.exists(path):
    fileName = os.path.basename(path)
    path_to_file = os.path.dirname(path)
    print(fileName)
    print(path_to_file)
else:
    print("The path does not exist")