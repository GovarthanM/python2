M = int(input())
m = set(map(int, input().split()))
N = int(input())
n = set(map(int, input().split()))
print('\n'.join(map(str, sorted(m.symmetric_difference(n)))))


#input: 2
#       1 2
#       5
#       2 3 4 5 6

#output: 1 3 4 5 6