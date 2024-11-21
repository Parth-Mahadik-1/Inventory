num1=int(input("enetr first number"))
num2=int(input("enetr second number"))
try:
    a=num1/num2
    print(a)
except ZeroDivisionError:
    print("infinite")