import re
text=input()
pattern='[A-Z][^A-Z]*'
m=re.findall(pattern,text)
print(m)