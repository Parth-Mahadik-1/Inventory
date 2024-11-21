class calculater:
    def __init__(self,num):
        self.num=num
    def squer(self):
        print(f"the squre of number{self.num}is {self.num**2}")

    def squreroot(self):
        print(f"the squreroot of number{self.num}is {self.num**0.5}")

    def cube(self):
        print(f"the cube of number{self.num}is {self.num**3}")
a=calculater(5)
a.squer()
a.cube()
a.squreroot()