import sys

string = sys.stdin.readline().strip() + ' '
stack = []
result = ''
cnt = 0

for i in string:
    if i == "<":
        cnt = 1
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)

    if i ==">":
        cnt = 0
        for _ in range(len(stack)):
            result += stack.pop(0)

    if i == " " and cnt == 0:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += " "
print(result)