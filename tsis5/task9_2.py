import re
text=input()
pattern='[A-Z][a-z]*'
m=re.findall(pattern,text)
print(' '.join(m))