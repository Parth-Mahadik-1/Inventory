import pandas as pd
import matplotlib.pyplot as plt
data={
    "subject":["c","C++","Python","Java"],
    "enroll":[58,32,88,62]
}

a=pd.DataFrame(data)
print(a)
plt.bar(data["subject"],data["enroll"],color="pink",edgecolor="cyan")
plt.title("Year 2024")
plt.xlabel("Subject")
plt.ylabel("Enroll")
plt.show()

