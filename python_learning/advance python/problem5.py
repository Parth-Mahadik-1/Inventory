n = int(input("enetr a number for multiplication table  you want:"))
l=[n*i for i in range(1,11)]
with open("table.txt","a") as f:
    f.write(str(l))
    f.write('\n')
