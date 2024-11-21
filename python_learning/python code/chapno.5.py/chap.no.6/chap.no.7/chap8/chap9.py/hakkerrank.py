class fizzbuzz:
    def my(self,n):
        a=[]
        for i in range (1,n+1):
            if i%3==0 and i%5==0:
                a.append("fizzbuzz")
            elif(i%3==0):
                a.append("fizz")
            elif(i%5==0):
                a.append("buzz")
            else:
                a.append(str(i))
        return a
obj=fizzbuzz()
p=obj.my(120)
print(p)        
    