a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a<b and a<c:
    print("the smallest is",a)
elif b<a and b<c:
    print("the smallest is",b)
else:
    print("the smallest is",c)