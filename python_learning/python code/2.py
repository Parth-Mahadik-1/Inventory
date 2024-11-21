import matplotlib.pyplot as p
import pandas  as pd
df = pd.DataFrame({"x":[1,2,3,4,5],"y":[4,5,6,8,9]})
#p.plot(df["x"],df["y"])
#for labling
p.xlabel("pressure")
p.ylabel("temp")
p.title("pressure and temp")


#p.scatter(df["x"],df["y"])
#bar graph
a = pd.DataFrame({"x":["m","n","p"],"y":[23,43,22]})
#p.bar(a["x"],a["y"],color="red")
#creating histogram
x =[1,2,3,4,5,6,3,2,2,1,2,3,2,1,4,5,2,1,4,5,4,4,2,3,2,]
#p.hist(x)
#pie chart

p.pie(a["y"],labels=a["x"])
p.show()

