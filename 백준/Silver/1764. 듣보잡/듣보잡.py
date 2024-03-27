import sys

n, m = map(int, sys.stdin.readline().split())
set_n = set()
for i in range(n):

    set_n.add(sys.stdin.readline().rstrip())

cnt = 0
result = set()
for i in range(m):
    name = sys.stdin.readline().rstrip()
    if name in set_n:
        cnt+=1
        result.add(name)

print(cnt)
for i in sorted(result):
    print(i)
