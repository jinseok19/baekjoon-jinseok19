import sys

n = int(sys.stdin.readline())
result = 0
for _ in range(n):
    cnt, apple = map(int, sys.stdin.readline().split())
    result += apple%cnt
print(result)
