import numpy as np

M1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9,]])
M2 = np.array([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9,]])
print(np.add(M1, M2))
print(np.subtract(M1, M2))
print(np.multiply(M1, M2))
print(np.divide(M1, M2))
print(np.sqrt(M1))


x = np.array([[1, 2,], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print(x.dot(y))
print(np.dot(x, y))
print(x@y)
print(np.matmul(x, y))


v1 = np.array([1, 2, 3])
v2 = np.array([-1, 3, -2])
print(np.dot(v1, v2))


xx = np.array([[1, 2], [3, 4], [5, 6]])
v1 = np.array([1, 2, 3])
print(np.dot(np.transpose(xx), v1))


data1 = np.arange(10)
print(data1)
print(np.average(data1))

data2 = np.arange(12).reshape(4, 3)
print(data2)
print(np.sum(data2, axis=0))
print(np.sum(data2, axis=1))


M11 = np.zeros((3, 3))
print(M11)

M12 = np.random.rand(3, 3)
print(M12)

M13 = np.linspace(0, 90, 10).reshape(2, 5)
print(M13)

M14 = np.eye(4)
print(M14)
