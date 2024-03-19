#X보다 작은수

import sys

N, X = map(int,sys.stdin.readline().split())



j = list(map(int,sys.stdin.readline().split()))
k = []
for i in range(N):
    if j[i] < X:
        k.append(j[i])

print(*k)