import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

yose = deque([i for i in range(1, N+1)])

result = []

while yose:
    yose.rotate(-(K-1))
    result.append(yose.popleft())

print(f'<{", ".join(map(str,result))}>')