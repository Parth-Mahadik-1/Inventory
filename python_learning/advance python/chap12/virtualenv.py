
def swapping(l1):
    size=len(l1)

    temp=l1[0]
    l1[0]=l1[size-1]
    l1[size-1]=temp
    return l1
l1=[12,34,23,45,43]
print(swapping(l1))