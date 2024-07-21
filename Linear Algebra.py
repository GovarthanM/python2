import numpy as np

def main():
    n = int(input("size of the matrix: "))
    A = np.array([input().split() for _ in range(n)], float)
    det = np.linalg.det(A)
    epsilon = 1e-10
    if abs(det) < epsilon:
        det = 0.0
    print(det)
if __name__ == '__main__':
    main()

# input: 3
#       1 2 3
#       4 5 6
#       7 8 9 


#output: 0.0 