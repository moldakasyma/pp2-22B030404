import re
text=input()
pattern='ab{2,3}'
m=re.search(pattern,text)
print(m)
