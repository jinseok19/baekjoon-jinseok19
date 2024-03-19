
import sys

t = int(sys.stdin.readline())

for _ in range(t):

    n = int(sys.stdin.readline())
    n_list = []
    n_list = map(int, sys.stdin.readline().split())
    print(sum(n_list))
