#sy4-05
p=1
n=eval(input("请输入整数值："))
for m in range(1,n+1):
    p*=m
print("{}的阶乘为:{}".format(n,p))
