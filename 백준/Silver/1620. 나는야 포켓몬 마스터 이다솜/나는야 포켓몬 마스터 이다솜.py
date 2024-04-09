import sys

n, m = map(int, sys.stdin.readline().split())
dogam = {}
for i in range(1, n+1):
    poket = sys.stdin.readline().rstrip()
    dogam[i] = poket
    dogam[poket] = i    

for _ in range(m):
    detect = sys.stdin.readline().rstrip()
    if detect.isdigit()== True:
        
        print(dogam[int(detect)])
    else:
        print(dogam[detect])