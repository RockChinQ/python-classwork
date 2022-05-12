def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True

lower=int(input("输入区间最小值:"))
upper=int(input("输入区间最大值:"))
ls=[]
if lower<=1 or upper<lower:
    print("输入有误")
else:
    for n in range(lower,upper):
        if isPrime(n):
            ls.append(n)

print("区间内有{}个素数".format(len(ls)))
print(ls)