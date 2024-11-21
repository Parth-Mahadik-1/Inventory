# self made logic program
def sum(n):
    if n == 0 or n == 1:
        return 1
    else:
        return sum(n-1)+n
A =5
f = sum(A)
print("sum is "+str(f))   

    