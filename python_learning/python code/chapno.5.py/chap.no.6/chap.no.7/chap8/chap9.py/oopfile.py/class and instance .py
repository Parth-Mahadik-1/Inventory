class employee:
    company="Google"
    salary=300
harry=employee()
#harry.salary=300 # this is instance attribute
harry.name="Harry"
print(harry.company)
employee.company="you  tube"
print(harry.company)
print(harry.salary)
print(harry.name)