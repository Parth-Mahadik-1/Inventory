while(True):
    print("press q to quite")
    a = input("enetr a number")
    if a=='q':
        break
  
    try:
        a=int(a)
        if a>6:
            print("your enter a greater number 6")
    except Exception as  e:
        print(f"your errors is {e}")

print("thanks for playing a game...")