import sys
import math
N, K = map(int, sys.stdin.readline().split())

def fac(n):
    res = math.factorial(n)
    return res
print(int(fac(N)/(fac(N-K)*fac(K))))