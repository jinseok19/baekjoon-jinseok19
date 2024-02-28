import sys

n_list = []
for _ in range(5):
    x = int(sys.stdin.readline())
    n_list.append(x)
sort_list = sorted(n_list)
print(int(sum(n_list)/5))
print(sort_list[2])