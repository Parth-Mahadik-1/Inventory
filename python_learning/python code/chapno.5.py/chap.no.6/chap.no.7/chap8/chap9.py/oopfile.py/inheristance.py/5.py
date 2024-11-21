import pandas as pd
import matplotlib.pyplot as plt
data={
    "Height":[58,59,60,61,62,63,64,65,66,67],
    "weight":[115,117,120,123,126,129,132,135,139,142]
}
a = pd.DataFrame(data)
print(a)
plt.plot(data["Height"],data["weight"])
plt.xlabel("height")
plt.ylabel("weight")
plt.show()