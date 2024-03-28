import sys

n, m = map(int, sys.stdin.readline().split())
site = {}

for _ in range(n):
    addr, ps = sys.stdin.readline().rstrip().split()
    site[addr] = ps


for _ in range(m):
    print(site[sys.stdin.readline().rstrip()])