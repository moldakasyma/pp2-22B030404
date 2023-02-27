import re
text=input()
pattern='[a-z]+_[a-z]+'
m=re.search(pattern,text)
print(m)