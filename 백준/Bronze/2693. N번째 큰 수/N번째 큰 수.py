import sys

t = int(sys.stdin.readline())

for _ in range(t):
    list_n = list(map(int, sys.stdin.readline().split()))
    list_n.sort()
    print(list_n[-3])