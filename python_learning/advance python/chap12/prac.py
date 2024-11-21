def amstrong(num):
    n1 = num 
    rem =0
    a =0
    while(n1>0):
        rem = n1%10
        a = a+(rem*rem*rem)
        n1 = n1//10
    if a == num:
        print("amstrong ")
    else:
        print("not amstrong")
amstrong(153)

