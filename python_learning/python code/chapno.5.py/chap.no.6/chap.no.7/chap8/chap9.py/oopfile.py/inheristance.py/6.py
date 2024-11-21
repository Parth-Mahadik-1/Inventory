def validate(num):
    if len(num)==10 and (num[0] in "8" or "9" or "7") and num.isdigit():
        return True
    else:
        return False
a = input("enter a number: ")
if validate(a):
    print("number is validate: ")
else:
    print("wrong number enter: ")