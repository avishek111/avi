#factorial of a number using recursion
def factor(num):
    if num==1:
        return 1
    else:
        return (num*(factor(num-1)))

num=int(input("Enter any number: "))
fact=factor(num)
print("The factorial is ",fact)

#WAP to print out first 20 fibonacci series starting from 1 using while loop
first_num=1
second_num=1
counter=1
while counter<=20:
    print(first_num,end=" ")
    third_num=first_num+second_num
    first_num=second_num
    second_num=third_num
    counter=counter+1

#WAP to print out first 20 fibonacci series starting from 1 using for loop
first_num1=1
second_num1=1
for i in range(0,20,1):
    print(first_num,end=" ")
    third_num1=first_num1+second_num1
    first_num1=second_num1
    second_num1=third_num1

#To print the numbers between 2000 and 3000 which are perfectly divisible by 7 and not a multiple of 5
first_num=2000
while first_num<=3000:
    mod=first_num%7
    mod1=first_num%5
    if mod==0 and mod1!=0:
        print(first_num,end=" ")
    first_num=first_num+

#To print the stars upto a user given limit
a=int(input("Enter any number: "))
b=1
while b<=a:
    print(b*"*")
    b=b+1

#LIST
num=[2,4,6,8,10]
print(num)

#num.append to insert a value at the last of the list
#num.insert(index,value) to insert a value at a specific position in a list

#To take five numbers as input to form a list and print the list as well as the sum of the numbers in the list
num=[]
a=int(input("Enter any numbers: "))
b=int(input("Enter any numbers: "))
c=int(input("Enter any numbers: "))
d=int(input("Enter any numbers: "))
e=int(input("Enter any numbers: "))
num.insert(0,a)
num.insert(1,b)
num.insert(2,c)
num.insert(3,d)
num.insert(4,e)
print(num)
counter=0
sum=0
while counter<=4:
    numb=int(num[counter])
    sum=sum+numb
    counter=counter+1
print(sum)

#To take 10 numbers as input and print the list as well as the largest among them, smallest among them and a list of odd numbers among them
#To take 10 numbers as input from the user and make a list of numbers in ascending order
odd=[]
ascend=[]
for i in range(0,10):
    num=int(input("Enter a number: "))
    ascend.insert(i,num)
counter=0
while counter<=9:
    numb=int(num[counter])
    mod=numb%2
    if mod==1:
        odd.insert(counter,numb)
    counter=counter+1
print(odd)

#To print a list of numbers in reverse order
num = [1, 2, 3]
rev=[]
counter = -1
pin = 0
while counter > -4:
    numb = int(num[counter])
    rev.insert(pin, numb)
    counter = counter - 1
    pin = pin + 1
print(rev)

#To take 10 numbers as input from the user and make a list of numbers in ascending order
ascend=[]
ascend1=[]
for i in range(0,10):
    num=int(input("Enter a number: "))
    ascend.insert(i,num)
counter=0
while counter<=9:
    num=min(ascend)
    ascend1.insert(counter,num)
    ascend.remove(num)
    counter=counter+1
print(ascend1)

#To take 10 numbg0ers as input from the user and make a list of numbers in ascending order
num=[5,4,3,2,1]
i=0
while i<5:
    j=0
    while j<4:
        if num[j]>num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp
        j=j+1
    i=i+1
print(num)
