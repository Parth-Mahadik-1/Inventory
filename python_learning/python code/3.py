import matplotlib.pyplot as plt

#x = [1, 2, 3, 4, 5]
#y = [2, 4, 4, 2, 8]
#plt.plot(x, y, '-.o')# '-o' specifies line with circles at data points

x =["audi","range rover","maruti","tata","macbeach","rolls royel"]
y=[20,10,30,11,20,35]
plt.pie(y,labels=x)
plt.show()
