#2618 - parth mahadik
# squear , rectangle , circale 
def u_input():
    print('''we have figures like
          1)square
          2)reactangle
          3)circle
''')
    s= int(input("enter ur choise"))
   
    
    if s==1:
        print("You are choosen an square figure... ")
        side = float(input("enter side of a square: "))
        print(f"Area of Square: {4*(side*side)}")
    elif s==2:
        print("You are choosen an rectangle figure... ")
        l= float(input("enter length of a rectangle: "))
        b = float(input("enter bridth of a rectangle: "))
        print(f"Area of Square: {l*b}")    
    elif s==3:
        print("You are choosen an circle figure... ")
        r= float(input("enter radius of a circle: "))
  
        print(f"Area of circle: {3.14*r*r}")
    else:
        print("figure not exits....")


if __name__=="__main__":
    u_input()        
        
    