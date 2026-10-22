import matplotlib.pyplot as plt;
import numpy as np;

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
y2 = [12, 18, 22, 28]

# categories = ["A", "B", "C"]
# values = [20, 35, 30]

data = np.random.randn(1000)
plt.figure(figsize=(8, 4), dpi=100)

# plt.plot(x, y, color="red", linewidth=2, linestyle="--", marker="o")
plt.plot(x, y, label="Product A")
plt.plot(x, y2, label="Product B")

# plt.scatter(x, y, s=50, c="green", alpha=0.7)
# plt.bar(categories, values)
# plt.barh(categories, values)
# plt.hist(data, bins=30)
# plt.boxplot(data)
# plt.pie(values, labels=categories, autopct="%1.1f%%")

# plt.title("Line Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()
