import sys

n = int(sys.stdin.readline())

n_list = list(map(int,sys.stdin.readline().split()))

sort_list = sorted(list(set(n_list)))

dic = {sort_list[i] : i for i in range(len(sort_list))}
for i in n_list:
    print(dic[i], end = ' ')
    

