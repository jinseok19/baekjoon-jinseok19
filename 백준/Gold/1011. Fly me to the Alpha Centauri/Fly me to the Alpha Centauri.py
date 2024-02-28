import sys

t = int(sys.stdin.readline())

for _ in range(t):
   
    x,y = map(int, sys.stdin.readline().split())
    distance = y-x
    count = 0
    move = 1
    k = 0
    while k < distance:
        count +=1
        k += move
        if count % 2 ==0:
            move +=1
    print(count)
            