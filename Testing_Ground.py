import numpy as np
matrix = np.array([
            [1, 2, 3],
            [2, 3, 4],
            ])

print(matrix)
print(matrix * 2)
print(-matrix + 2)
print(np.exp(matrix))
print(matrix * matrix)


depth = 3
for i in range(depth - 2, 0, -1):
    print(i)


a = np.inf
print(a)
if a > 1000000000000:
    print("a > 1000000000000")



a = []
b = [[1,2],[3,4]]
c = 2
a = b
a = c

print(a)
print(b)
print(c)
print(np.sum(b))
print(sum([1,2]))