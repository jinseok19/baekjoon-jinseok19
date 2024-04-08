import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = 0
    sum_g = 0
    for _ in range(n):
        c,g = map(float,sys.stdin.readline().split())
        cnt += c
        sum_g +=g * c
    print(int(cnt), round(sum_g/cnt,1))