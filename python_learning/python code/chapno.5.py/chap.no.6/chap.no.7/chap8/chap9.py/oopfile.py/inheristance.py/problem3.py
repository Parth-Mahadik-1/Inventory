class employee:
    salary= 500
    salaryIncrement=2
    @property
    def salaryAfterIncrement(self):
        return (self.salary*self.salaryIncrement)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,val):
        self.salaryIncrementn= val/self.salary
e=employee()
print(e.salaryAfterIncrement)
print(e.salaryIncrement)
