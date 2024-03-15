
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    start = [i for i in range(1,n+1)]
    for j in range(k):
        for z in range(1,n):
            start[z] += start[z-1]
    print(start[-1])
