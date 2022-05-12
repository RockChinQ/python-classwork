def getNum():
    nums=[]
    iNumStr=input("请输入数字(直接输入回车退出):")
    while iNumStr!="":
        nums.append(eval(iNumStr))
        iNumStr=input("请输入数字(直接输入回车退出):")
    return nums

def mean(numbers):
    s=0.0
    for num in numbers:
        s+=num
    return s/len(numbers)
n=getNum()
m=mean(n)
print("平均值:{:.2f}".format(m))