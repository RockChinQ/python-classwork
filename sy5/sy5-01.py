#sy5-01.py  count characters with for
ss = input("请输入一个字符串：")
c = input("请输入一个字符：")
cnt = 0
for i in ss:
    if i==c:
        cnt+=1    
print("{}中有{}个{}。".format(ss,cnt,c))
