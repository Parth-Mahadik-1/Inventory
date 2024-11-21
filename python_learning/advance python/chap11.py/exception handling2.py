while(True):
  print("press q to quite")
  a = input("enetr a number")
  if a=='q':
    break
  try:
    a=int(a)
    if a>6:
     print("your enter a greater number")
  except Exception as e:
    print(f"the error is : {e}")
print("thanks for playing a game...")