import numpy as np

A = np.array(input().split(), int)
B = np.array(input().split(), int)
print(np.inner(A, B))
print(np.outer(A, B))



#input: 1 2 3
#       4 5 6



#output: 32
#        [[ 4  5  6]
#         [ 8 10 12]
#         [12 15 18]]
