import re
text=input()
def camel_snake(text):
    st=re.sub('(.)([A-Z][a-z]+)',r'\1_\2',text)
    return re.sub('([a-z0-9])([A-Z])',r'\1_\2',st).lower()
print(camel_snake(text))