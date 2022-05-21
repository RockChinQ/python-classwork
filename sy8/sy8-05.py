score=float(input("百分制成绩:"))
grade="E"

if score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=69:
    grade="D"

print("等级:{}".format(grade))
