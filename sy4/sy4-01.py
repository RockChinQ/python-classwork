#sy4-01.py prime number judgment
n = eval(input("请输入一个整数："))
for i in range(2,n):
    if n % i == 0:
        print("{}不是素数！".format(n))
        break
else:
    print("{}是素数！".format(n))