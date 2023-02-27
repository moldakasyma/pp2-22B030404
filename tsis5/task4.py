import re
text=input()
pattern='[A-Z][a-z]+'
m=re.search(pattern,text)
print(m)