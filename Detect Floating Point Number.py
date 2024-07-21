import re
for _ in range(int(input())):
    print(bool(re.match(r'^[+-]?\d*?\.\d+$', input())))

#input: 2
#       5
#       1.2


#output: False
#        True