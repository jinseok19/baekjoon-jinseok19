import sys

n, m = sys.stdin.readline().rstrip().split()
n, m = list(map(int,n)),list(map(int,m))

print(sum(n) * sum(m))