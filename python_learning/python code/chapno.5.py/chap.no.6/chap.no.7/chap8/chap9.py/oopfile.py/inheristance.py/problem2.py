class animals:
    p  = "germen sheffed"

class pets(animals):
    color="greay"

class dog(pets):
    def bark():
        print("BoW BoW!")
d= dog
print(d.p)
print(d.color)
d.bark()