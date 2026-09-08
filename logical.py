#logical operators
age=25
citizen=True
print(age>=18 and citizen == True)
age=16
citizen=True
print(age>=18 and citizen == True)

has_card = False
has_cash = True
print(has_card or has_cash)



#atm eligibility checker
balance = 10000
withdraw =5000
print(withdraw > 0 and withdraw <= balance)

#student scholorship eligibility checker
marks = float(input("Enter marks:"))
attendence = float (input("Enter attendence:"))
eligible = marks >= 85 and attendence >=75
print("Scholorship Eligible:",eligible)

#identity operators
a = None
print(a is None)
print(a is not None)

#bitwise operators
a = 5
b = 3
print(a&b)
print(a|b)
print(a^b)

#electricity city bill calculator
units = int(input("enter electricity units:"))
rate = 6
bill = units * rate 
print("electricity bill :",bill)

#travel expense calculator 
travel = float(input("Travel expense:"))
food = float(input("Food expense:"))
hotel = float(input("hotel expense:"))
total = travel + food + hotel
print("Total Expense:",total)