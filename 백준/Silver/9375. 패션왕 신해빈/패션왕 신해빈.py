import sys
from collections import Counter

t = int(sys.stdin.readline())

for _ in range(t):
    cnt = Counter()
    n = int(sys.stdin.readline())

    for _ in range(n):
        fa, po = sys.stdin.readline().rstrip().split()
        cnt[po] +=1
    
    c = 1
    for key in cnt:
        c *= cnt[key]+1
    
    print(c-1)