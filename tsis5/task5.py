import re
pattern='[a].*[b]'
text=input()
m=re.search(pattern,text)
print(m)