import sys
N = int(sys.stdin.readline())

list_n = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())
print(list_n.count(k))
