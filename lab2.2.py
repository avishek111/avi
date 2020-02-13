a=int(input("enter the no of first subject"))
b=int(input("enter the no of second subject"))
c=int(input("enter the no of third subject"))
d=int(input("enter the no of fourth subject"))
percent=(a+b+c+d)/4
if percent>70:
    print("distinctioin")
elif percent>60:
    print("first")
elif percent>50:
    print("second")
elif percent>40:
    print("pass")
else:
    print("fail")