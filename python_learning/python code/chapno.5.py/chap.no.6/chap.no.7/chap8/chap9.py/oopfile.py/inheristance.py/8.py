import re
str=input("Enter a password: ")
pat = ("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,10}")

validate = re.match(pat,str)
if validate:
    print("password validation succefully")
else:
    print("wrong password")