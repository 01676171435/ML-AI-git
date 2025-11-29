import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 7]

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()


plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()


categories = ['A', 'B', 'C', 'D']
values = [15, 28, 12, 20]
plt.bar(categories, values)
plt.xlabel("Catagories")
plt.ylabel("Values")
plt.title("Bar Chart")
plt.show()


data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5)
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()


dates = pd.date_range(start='2024-01-01', periods=10, freq='D')
values = [10, 12, 15, 13, 16, 18, 17, 20, 22, 21]
plt.plot(dates, values)
plt.xlabel("Data")
plt.ylabel("Value")
plt.title("Time Series Plot")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

x = np.arange(0, 10, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine Curves")
plt.legend()
plt.show()
