try:
    i=int(input("enetr a number"))
    c=1/i
except Exception as e:
    print(e)
    exit()
finally:
    print(" Thanks for using code:....")