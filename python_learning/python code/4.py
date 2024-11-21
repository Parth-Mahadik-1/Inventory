import re

str =input("enter pass word: ")
pat=("(?=.*[a-z])(?=.*)[A-Z](?=.*\d)(?=.*[@$%*?&]).{8,10}")
validate=re.match(pat,str)
if validate:
    print("pass word validation succesfully:")
else:
    print("wrong password")