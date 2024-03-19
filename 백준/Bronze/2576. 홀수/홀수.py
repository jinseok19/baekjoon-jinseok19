import sys
n_list = []
for i in range(7):
    x = int(sys.stdin.readline())

    if x%2 == 1:
        n_list.append(x)
if len(n_list)==0:
    print(-1)
else:
    print(sum(n_list))
    print(min(n_list))    