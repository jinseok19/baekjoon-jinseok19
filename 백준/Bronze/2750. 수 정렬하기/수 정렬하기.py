import sys

n = int(sys.stdin.readline())
n_list = []
for _ in range(n):
    x = int(sys.stdin.readline())
    n_list.append(x)

for i in sorted(n_list):
    print(i)