import re
text=input()
pattern='^a[0(b*?)]$'
m=re.search(pattern,text)

print(m)
