import re
text=input()
def snake_camel(text):
    t=re.findall('[a-z]+',text)
    c=""
    for i in t:
        c+=i[0].upper()+i[1:len(i)]
    return c

print(snake_camel(text))
    