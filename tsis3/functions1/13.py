import random
s=input('Hello! What is your name?\n')
print('Well,',s,',','I am thinking of a number between 1 and 20.')
gn=random.randint(1,20)
n=int(input('Take a guess\n'))
count=1
while n!=gn:
    if n<gn:
        print('Your guess is too low.')
    elif n>gn:
        print('Your guess is too high.')
    n=int(input('Take a guess\n'))
    count+=1
    
dj='Good job,{name}!You guessed my number in {cnt} guesses!'
print(dj.format(name=s,cnt=count))   

