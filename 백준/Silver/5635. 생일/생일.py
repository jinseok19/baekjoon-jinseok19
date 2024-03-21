import sys

t = int(sys.stdin.readline())
n_list = []

for _ in range(t):
    name, day, month, year = sys.stdin.readline().rstrip().split()
    n_list.append([name, int(year), int(month), int(day)])

n_list.sort(key= lambda x: (x[1], x[2], x[3]))

print(n_list[-1][0])
print(n_list[0][0])

