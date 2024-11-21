print("************************** GUSSE THE NUMBER *********************************")
import random
 
randno = random.randint(1, 5)

usergusse= None
gus=0
while(usergusse != randno):
    usergusse= int(input("Enter YOur Gusse :"))
    gus+=1

    if  ( usergusse==randno):
      print("Your gusse is right :")
    else:
        if(usergusse>randno): 
            print(" Your Gusse Is Wronged ! Enter a smaller  Number : ")
        else:
            print(" Your Gusse Is Wronged ! Enter A Larger Number :")

print(f"Your Gusse the number in** {gus} ** gusseses")
try:
    with open("C:\\Users\\Parth\\Desktop\\python code\\chapno.5.py\\chap.no.6\\chap.no.7\\chap8\\chap9.py\\oopfile.py\\inheristance.py\\kfop.txt", "r") as f:
        data = f.read()
        hiscore = int(data) if data.strip() else float('inf')
except FileNotFoundError:
    hiscore = float('inf')  # Set a very high default high score for the first run

# Check if the player broke the high score and update the file if necessary
if gus < hiscore:
    print("You Just Broke The High Score!")
    with open("C:\\Users\\Parth\\Desktop\\python code\\chapno.5.py\\chap.no.6\\chap.no.7\\chap8\\chap9.py\\oopfile.py\\inheristance.py\\kfop.txt", "w") as f:
        f.write(str(gus))
    


    










