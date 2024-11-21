import re

phone = input("Enter landline phone number: ")
pat = r"^[789]\d{9}$"
validate = re.match(pat, phone)

if validate:
    print("Phone number is valid.")
else:
    print("Invalid phone number.")

