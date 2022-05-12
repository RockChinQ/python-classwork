def gcd(num1,num2):
    m=max(num1,num2)
    n=min(num1,num2)
    r=m%n

    while r!=0:
        m=n
        n=r
        r=m%n
    
    return n

num1=int(input("第一个数字:"))
num2=int(input("第二个数字:"))

print("{}和{}的最大公约数为:{}".format(num1,num2,gcd(num1,num2)))