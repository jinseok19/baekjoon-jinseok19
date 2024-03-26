import sys
from collections import deque

n = int(sys.stdin.readline())

list_n = []
deque_n = deque(range(1, n+1))

while len(deque_n) !=1: 
    list_n.append(deque_n.popleft())
    deque_n.append(deque_n.popleft())
list_n.append(deque_n[0])

print(*list_n)