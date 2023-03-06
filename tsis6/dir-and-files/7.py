with open("all.txt") as f:
    with open ("new.txt","w") as f1:
        for x in f:
            f1.write(x)