#sy4-02.py prime number judgment
sum=0
for n in range(0,50):
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        print("{} ".format(n),end="")
        sum+=n
print("\n{}".format(sum))
