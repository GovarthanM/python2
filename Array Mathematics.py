import numpy as np

n, m = map(int, input().split())
A = np.array([input().split() for _ in range(n)], int)
B = np.array([input().split() for _ in range(n)], int)
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)

#input : 2 2
#        1 2
#        3 4
#        5 6
#        7 8