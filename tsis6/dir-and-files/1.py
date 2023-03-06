import os
root =os.path.abspath(input())


directory = open("directory.txt", "x")
directory.write("list of only directories:\n")

directory.close()

file = open("files.txt", "x")
file.write("list of only files:\n")

file.close()
all = open("all.txt", "x")
all.write("list of all directories and files:\n")

all.close()
