import random

print("***********************GUSSE THE NUMBER*******************************")

randno=random.randint(1,5)
usergusse=None
gusses=0
while(usergusse!=randno):
 #take input from user   
    usergusse= int(input("enetr your gusse: "))
    gusses+=1
    if(usergusse==randno):
        print("Your gusse is correct ")
    else:
        if(usergusse>randno):
            print("your gusse is wrong , enter a smaller number")
        else:
            print("your gusse is wrong , enter a smaller number")

print(f"you gusse the number in **{gusses}**")

try:
    with open("C:\\Users\\Parth\\Desktop\\python code\\chapno.5.py\\chap.no.6\\chap.no.7\\chap8\\chap9.py\\oopfile.py\\inheristance.py\\kfop.txt","r") as f:
        data=f.read() 
        highscore=int(data) if data.strip() else float('inf')
except FileNotFoundError:
    highscore=float('inf')

if(gusses<highscore):
    print("you just broke highscore!!!")
    with open("C:\\Users\\Parth\\Desktop\\python code\\chapno.5.py\\chap.no.6\\chap.no.7\\chap8\\chap9.py\\oopfile.py\\inheristance.py\\kfop.txt","w") as f:
        f.write(str(gusses))