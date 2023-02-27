import re
pattern='[ ,.]'
text=input()
m=re.sub(pattern,':',text)
print(m)