import sys

n = int(sys.stdin.readline())
n_list = []
for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    n_list.append((x,y))

for i in sorted(n_list):
    print(*i)
    
    