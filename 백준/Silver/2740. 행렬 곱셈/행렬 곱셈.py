import sys

n1, m1 = map(int, sys.stdin.readline().split())
a = []
b = []
result = []
for i in range(n1):
    d1 = list(map(int, sys.stdin.readline().split()))
    a.append(d1)


n2, m2 = map(int, sys.stdin.readline().split())
for i in range(n2):
    d2 = list(map(int, sys.stdin.readline().split()))
    b.append(d2)


c = [[0 for _ in range(m2)] for _ in range(n1)]

for n in range(n1):
    for k in range(m2):
        for m in range(m1):
            c[n][k] += a[n][m] * b[m][k]

for i in c:

    print(*i)
