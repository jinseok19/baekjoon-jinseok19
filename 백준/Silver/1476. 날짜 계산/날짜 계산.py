import sys

E, S, M = map(int,sys.stdin.readline().split())

y = 1

while True:
    if (y-E)%15 == 0 and (y-S)%28==0 and (y-M)%19==0:
        break
    y +=1

print(y)