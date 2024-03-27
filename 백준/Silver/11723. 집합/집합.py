import sys

m = int(sys.stdin.readline())
all_1 = [i for i in range(1,21)]

S = set()
for i in range(m):
    cmd = sys.stdin.readline().rstrip().split()
       
    if cmd[0] =="add":
        S.add(int(cmd[1]))

    elif cmd[0] =="check":
        if int(cmd[1]) in S:
            print(1)
        else:
            print(0)


    elif cmd[0] == "remove":
        S.discard(int(cmd[1]))

    elif cmd[0] =="toggle":
        if int(cmd[1]) in S:
            S.discard(int(cmd[1]))
        else:
            S.add(int(cmd[1]))

    elif cmd[0] == "all":
        S.update(all_1)

    elif cmd[0] == 'empty':
        S = set()


