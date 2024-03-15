import sys

n = int(sys.stdin.readline())

for i in range(n):
    stack = []
    k = sys.stdin.readline().rstrip()

    for j in k:
        if j =="(":
            stack.append(j)
        elif j==")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
    