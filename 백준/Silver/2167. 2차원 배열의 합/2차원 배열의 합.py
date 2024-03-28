import sys

n, m = map(int, sys.stdin.readline().split())
list_n = []
for _ in range(n):
    list_n.append(list(map(int, sys.stdin.readline().split())))

cmd = int(sys.stdin.readline())

for _ in range(cmd):
    toSum = list(map(int,sys.stdin.readline().split()))
    s = 0
    for j in range(toSum[0]-1, toSum[2]):
        for k in range(toSum[1]-1, toSum[3]):
            s += list_n[j][k]
    print(s)