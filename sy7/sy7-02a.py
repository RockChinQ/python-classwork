n=int(input("输入一个整数:"))
result=1
for i in range(1,n+1):
    result*=i

print("结果:{}".format(result))