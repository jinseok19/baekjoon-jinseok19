import sys

N = int(sys.stdin.readline().rstrip())
n_list = ['3','6','9']
result = 0

for i in range(1,N+1):
    str_i = str(i)
    for j in str_i:
        if j in n_list:
            result+=1

print(result)