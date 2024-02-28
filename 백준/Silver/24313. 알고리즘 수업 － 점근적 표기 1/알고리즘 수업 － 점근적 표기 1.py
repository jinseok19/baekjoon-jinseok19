import sys

a1, a0 = map(int,sys.stdin.readline().split())

c = int(sys.stdin.readline())

n0 = int(sys.stdin.readline())
ex1 = a1*n0 + a0
ex2 = c*n0
if ex1<=ex2 and a1<=c:
    print(1)
else:
    print(0)