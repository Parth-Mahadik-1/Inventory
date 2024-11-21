def validate(password):
    c = 0
    
    if len(password)>=8:
    
        c=c+1
        
    for i in password: # parth@1234Mahadik
        if i.upper():
            
            c=c+1
            break
    for i in password:
        if i=="!" or "@" or "#" or "$" or "%" or "^" or "&":
        
            c=c+1
            break
    for i in password:
        if i.isdigit():
          
            c=c+1
            break

    if c == 4:
        
        return True
    else:
        
        return False
    
p = input("enter a password: ")

if validate(p):
    print("Password validate succefully")
else:
    print("wrong password")
        
