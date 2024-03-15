import sys
from collections import deque
N = int(sys.stdin.readline())
deque = deque()

for _ in range(N):
    cmd = list(sys.stdin.readline().rstrip().split())

    if cmd[0] == "push":
        deque.append(cmd[1])
    elif cmd[0] == "pop":
        if len(deque) > 0:
            s = deque.popleft()
            print(s)
        else:
            print(-1)
    elif cmd[0] =="size":
        print(len(deque))
    elif cmd[0] == "empty":
        if len(deque)>0:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if len(deque) > 0:
            print(deque[0])
        else:
            print(-1)

    elif cmd[0] == "back":
        if len(deque) > 0:
            print(deque[-1])
        else:
            print(-1)


