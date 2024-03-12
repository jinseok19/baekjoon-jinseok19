import sys

N = sys.stdin.readline().rstrip()
F = int(sys.stdin.readline())

num = int(N[:-2]+"00")

while True:
    if num % F ==0:
        break
    num +=1

print(str(num)[-2:])
