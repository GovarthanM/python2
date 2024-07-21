for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)


#input: 3
#       10 5
#       10 0
#       10 a


#output: Error Code: integer division or modulo by zero

#        Error Code: invalid literal for int() with base 10: 'a'
