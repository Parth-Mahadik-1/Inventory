class c2dvec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"
class c3dvec(c2dvec):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"

c2d=c2dvec(2,5)
c3d=c3dvec() 
print(c2d)
print(c3d)   
    

    