# self logic devlop program

class vector:
    def __init__(self,i, j, k):
        self.icap=i
        self.jcap=j
        self.kcap=k
    def __add__(self,c,):
        return vector(self.icap + c.icap,self.jcap +c.jcap,self.kcap+c.kcap)
   
   
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"
    
    def __mul__(self, c):
      
      
        return vector(self.icap * c.icap,self.jcap * c.jcap,self.kcap*c.kcap)

v=vector(1,2,1)
v2=vector(2,3,2)
print("vector are::\n")
print(v)
print(v2)
print("The Addition of vector is:: \n")
print(v+v2)
print("The multipication is : \n" )
print(v*v2)