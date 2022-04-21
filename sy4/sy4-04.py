#sy4-04.py
num1=int(input("请输入第一个数字:"))
num2=int(input("请输入第二个数字:"))
m=max(num1,num2)
n=min(num1,num2)
r=m%n
while r!=0:
    m=n
    n=r
    r=m%n
print("{}和{}的最大公约数为:{}".format(num1,num2,n))
print("{}和{}的最小公倍数为:{}".format(num1,num2,num1*num2//n))
