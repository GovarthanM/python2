import numpy as np

P = np.array(input().split(), float)
x = float(input())
print(np.polyval(P, x))

#input: 1 3 0    4

#output: 28.0