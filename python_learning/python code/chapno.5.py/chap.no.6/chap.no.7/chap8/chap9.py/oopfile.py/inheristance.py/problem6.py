class vector:
    def __init__(self,vec):
        self.vec =vec 
    
    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
    
v1= vector([1,4,5])
v2 = vector([4,5,6])
print(v1)
print(v2)