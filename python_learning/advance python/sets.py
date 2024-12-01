#creation of set
a = { 1 , 2, 3, 4,1,2,3}
print(type(a))
print(a)

print(f"lenght of set {len(a)}")
print(f"minimum  value of set {min(a)}")
print(f"maximum value of set {max(a)}")
print(f"sort set {sorted(a)}")
print(f"sum of elements {sum(a)}")


b = { 1 , 2, 3, 4,1,2,3,"Parth","chinmay",0.55}
print(type(b))
print(b)

b.add('Hello')
# using for loop
for i in b:
    print(f"elemnt  : {i}")

b.remove("Hello")
print(b)

b.clear()
print(b)

#mathmatical set operations

manger = {"Parth","chinmay","yogi","viraj","joshi","sopara"}
hr = {"yogi","joshi","gulab"}

#Union
print(manger | hr)


#intersection
print(manger & hr)


#diff
print(manger-hr)




