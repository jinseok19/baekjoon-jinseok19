import sys
N,M = map(int,sys.stdin.readline().split())

a, b = [], []

for row in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    a.append(row)

for row in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    b.append(row)

for row in range(N):
    for col in range(M):
        print(a[row][col] + b[row][col], end= ' ')
    print()