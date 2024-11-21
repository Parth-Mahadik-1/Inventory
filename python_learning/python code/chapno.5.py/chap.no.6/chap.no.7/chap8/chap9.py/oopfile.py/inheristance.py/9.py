import pandas as yogesh 
import matplotlib.pyplot as yogi
data={"height":[58,59,60,61,62,63,64,65,66,67],
"weight":[115,117,120,123,126,129,132,135,139,142]}

a=yogesh.DataFrame(data["weight"],data["height"])
print(a)

yogi.plot(a)
yogi.xlabel("height")
yogi.ylabel("weight")
yogi.title("height vs weight")
yogi.show()



