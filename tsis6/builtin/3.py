mystr=input()
def ispali(mystr):
    if mystr==mystr[::-1]:
        return True
    else:
        return False
    
print(ispali(mystr))