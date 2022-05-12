def fac(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

print("s=3!+5!+7!={}".format(fac(3)+fac(5)+fac(7)))