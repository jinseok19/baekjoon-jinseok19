n = int(input())
n_list = []

for i in range(n):
  n_list.append(input())
n_set_list = set(n_list)
n_list = list(n_set_list)

n_list.sort()
n_list.sort(key= len)

for i in n_list:
  print(i)
