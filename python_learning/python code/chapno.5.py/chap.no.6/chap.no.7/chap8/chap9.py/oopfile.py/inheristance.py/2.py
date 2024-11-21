s1 = float(input("Enter 1st side of triangle"))
s2 = float(input("Enter 2nd side of triangle"))
s3 = float(input("Enter 3rd side of triangle"))
if s1 != s2 != s3:
    print("According to input triangle will be scales trinalge.. ")
elif s1 == s2 or s2==s3 or s1== s3:
    print("According to input triangle will be isoscales trinalge.. ")
if s1 == s2 == s3:
    print("according to input triangle will be equilateral...")