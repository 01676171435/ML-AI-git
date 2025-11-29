

import numpy as np
import pandas as pd

list1 = [[1, 0], [1, 1], [2, 2], [2, 3], [2, 3],
         [2, 4], [3, 4], [3, 5], [4, 6], [5, 7]]
print(list1)

df_list1 = pd.DataFrame(list1, columns=['x', 'y'])
print(df_list1)


df_list1.hist(column=['x'], bins=5)


print('Skew: ', df_list1[['x']].skew())

df_list1.hist(column=['y'], bins=8)
print('Skew: ', df_list1[['y']].skew())


print('Kurt - X: ', df_list1[['x']].kurt())
print('Kurt - Y: ', df_list1[['y']].kurt())


df_list1.plot.scatter(x="x", y="y")
df_list1.boxplot(column=['x', 'y'])


A = np.array([1, 2, 3, 4, 5, 6,])
print(A)

B = np.array([10, 20, 30, 40, 50, 60,])
print(B)

print(A+B)
print(A-B)

list1 = [1, 2, 3, 4, 5, 6]
print(list1)

list2 = [10, 20, 30, 40, 50, 60]
print(list2)


print(list1+list2)

# print(list1-list2) unsuported '-'


temp = np.array([10, 15, 20, 5, 30, 37])
temp_fahrenheit = temp * 1.8+32
print(temp_fahrenheit)


M1 = np.array([[1, 2, 3], [4, 5, 6]])

M2 = np.array([[7, 8, 9], [3, 4, 5]])


print(M1)
print(M2)
print(M1.shape)

M3 = M1+M2
M4 = M1-M2
M5 = M1*M2
M6 = M1/M2

print(M3)

print(M4)

print(M5)

print(M6)

M7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9,]])

M7 = M7[:, 0:2]
print(M7)

M7 = M7[-1, -2:]
print(M7)
