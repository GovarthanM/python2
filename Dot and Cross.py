import numpy as np

n = int(input())
A = np.array([input().split() for _ in range(n)], int)
B = np.array([input().split() for _ in range(n)], int)
print(np.dot(A, B))


#input : 2
#        1 2
#        3 4
#        5 6
#        7 8

#output: [[19 22]
#         [43 50]]
