def input_data():
    name = input("enter a name : ")
    id = int(input("enter a id: "))
    return name,id



while(True):
    print('''
    1 - input
    2- exit
    ''')
    a = int(input())
    if a == 2:
        print("exiting......")
        break
    elif a == 1:
        print(input_data())
    else:
        print("ivalid inout...")


