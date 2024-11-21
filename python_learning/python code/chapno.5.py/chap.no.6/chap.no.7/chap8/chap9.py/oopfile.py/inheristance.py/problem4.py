#(a+bi)(c+di)=(ac-bd)+(ad+bc)i

class complex:
    def __init__(self, r,i):
        self.real=r
        self.imagnery=i

    def __add__(self,c):
        return complex(self.real + c.real,self.imagnery + c.imagnery)
    
    def __mul__(self,c):
        mulReal= self.real*c.real-self.imagnery*c.imagnery
        mulimg= self.real*c.imagnery+self.imagnery*c.real
        return complex(mulReal,mulimg)

    def __str__(self):
        return f"{self.real}+{self.imagnery}i"
    
c1=complex(1, 2)
c2=complex(-2, 1)
#print("addtion is: ",c1+c2)
print("multiplication is: ",c1*c2)
