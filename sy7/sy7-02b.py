def fac(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

print("结果:{}".format(fac(int(input("输入一个整数:")))))