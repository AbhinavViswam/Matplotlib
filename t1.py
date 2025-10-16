import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
y1 = [2,4,6,8,10]
y2 = [1,3,5,7,9]
categories = ["A","B","C","D"]
values = [10,12,35,4]
a = np.random.rand(50)
b = np.random.rand(50)
sizes = [30,40,20,10]
labels = ["Apple","Banana","Citrus","Dragonfruit"]

# plt.plot(x,y)
# plt.title("Plot")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")

# plt.plot(x,y,color="red", linestyle="--", marker="o")
# plt.grid(True)
# plt.show()


# plt.plot(x,y1, label="Even" , color="red" , marker="*")
# plt.plot(x,y2,label="Odd", color="blue", marker="o")
# plt.legend()
# plt.grid(True)
# plt.show()

# bar

# plt.bar(categories,values,color="purple")
# plt.title("Categories and values")
# plt.show()

# plt.scatter(x,y, color="red")
# plt.show()

# histogram

data = np.random.randn(1000)
# plt.hist(data,bins=50,color="skyblue", edgecolor="black")
# plt.show()

# pie chart

# plt.pie(sizes,labels=labels, autopct="%1.1f%%", startangle = 90)
# plt.show()


# fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# axs[0, 0].plot(x, y1, color="red")
# axs[0, 1].bar(categories, values, color="orange")
# axs[1, 0].scatter(x, y2, color="blue")
# axs[1, 1].hist(data, bins=20, color="green")

# plt.tight_layout()
# plt.show()


df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [250, 300, 400, 350]
})

# df.plot(x="Month",y="Sales",kind="bar")
df.plot(x="Month",y="Sales",kind="pie")
plt.show()