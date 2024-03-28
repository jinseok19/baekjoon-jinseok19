import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] =='1':
        stack.append(int(cmd[1]))
    elif cmd[0] =='2':
        if len(stack)==0:
            print(-1)
        else:
            k=stack.pop()
            print(k)
    elif cmd[0]=='3':
        print(len(stack))

    elif cmd[0] =='4':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif cmd[0] =='5':
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)