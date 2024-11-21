sub1 = int(input("enetr sub1: "))
sub2 = int(input("enetr sub2: "))
sub3 = int(input("enetr sub3: "))

if (sub1<33 or sub2<33 or sub3<33):
    print("you are fail")

elif(sub1+sub2+sub3<40):
    print("you are fail")
else:
    print("you are passed")