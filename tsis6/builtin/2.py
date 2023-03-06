mystr=input()
count1=0
count2=0
for x in mystr:
    if x.isupper():
        count1+=1
            

    else:
        count2+=1
    
print(count1,count2)