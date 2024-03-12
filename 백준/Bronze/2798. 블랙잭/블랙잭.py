import sys
N,M = map(int,sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if n_list[i] + n_list[j] + n_list[k] > M:
               pass
            else:
               result = max(result, n_list[i] + n_list[j] + n_list[k])
print(result)
