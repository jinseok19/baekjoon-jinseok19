import sys

n = int(sys.stdin.readline())
size = 0
paper = [[0]*101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1

for i in paper:
    size += sum(i)

print(size)