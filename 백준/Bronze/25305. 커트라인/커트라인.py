import sys
n,k = map(int,sys.stdin.readline().split())
x = list(map(int,sys.stdin.readline().split()))
    
sort_list = sorted(x)
print(sort_list[-k])