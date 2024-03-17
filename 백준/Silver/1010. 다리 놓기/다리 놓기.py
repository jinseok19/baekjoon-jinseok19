import sys
import math

def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))


t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())

    print(nCr(b,a))