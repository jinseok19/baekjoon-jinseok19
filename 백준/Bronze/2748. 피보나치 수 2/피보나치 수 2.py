import sys
 
n = int(sys.stdin.readline())

a1 = 0
a2 = 1
result = 0
if n == 0 or n ==1:
    print(n)
else:

    for _ in range(n-1):
        result = a1 + a2
        a1 = a2
        a2 = result

    print(result)