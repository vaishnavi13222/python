num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


marks  = int(input("enter a number"))
if marks>=35:
    print(marks,"pass")
else:
    print(marks ,"fail")

number= int(input("enter a number:"))
if number%5==0:
    print("divisible by 5")

#TEMPERATURE CHECK
temperature = float(input("enter temperature:"))
if temperature >40:
    print("high temperature")

number = int(input("enter a number:"))
if number>100:
    print("number is  greater than 100")
else:
    print(" number is less than 100")

number = int(input ("enter a number "))
if number>=0:
    print("positive")
else:
    print("negative")

marks=int(input("enter marks:"))
if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=60:
    print("grade C")
elif marks>=40:
    print("grade D")
else:
    print("fail")

a=int(input("enter first number:"))
b=int(input("enter second number:"))
if a>b:
    print("largest:", a)
elif b>a:
    print("largest:",b)
else:
    print("both are equal")

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b and a>=c:
    print("largest:",c)
elif b>=a and b>=c:
    print("largest:",b)
else:
    print("largest:",c)

number = int(input("enter a number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

day = int(input("enter day number:"))
if day==1:
    print("sunday")
elif day==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("thursday")
elif day==6:
    print("friday")
elif dqay==7:
    print("saturday")
else:
    print("invalid day")

a=float(input("enter first number:"))
b=float(input("enter second number:"))
operator=input("enter operator(+,-,*,/):")
if operator == "+":
    print("results:",a+b)
elif operator =="-":
    print("results:",a-b)
elif operator == "*":
    print("results:",a*b)
elif operator=="/":
    if b !=0:
        print("result:",a/b)
else:
    print("cannot divide by zero")

username=input("enter username:")
password=input("enter password:")
if username== "admin":
    if password=="6723":
        print("login successful")
    else:
        print("wrong password")
else:
    print("wrong username")

#balance input
balance = float(input("enter balance:"))
amount = float(input("enter withdrawal amount:"))
if amount > 0:
    if amount <= balance:
        balance = balance - amount
        print("withdrawal successful")
        print("remaining balance:", balance)
    else:
        print("insufficient balance")
else:
    print("invalid amount")

marks = int(input("enter marks:"))
attendence  = float(input("enter attendence percentage:"))
if marks  >=40:
    if attendence>=75:
        print("eligible")
    else:
        print("not eligible due to attendence")
else:
    print("fail")

age=int(input("enter your age"))
test= input("did you pass the driving test? (yes/no):")
if age >18:
    if test=="yes":
        print("license can be issued")
    else:
        print("pass the driving test first")
else:
    print("not eligible due to age ")