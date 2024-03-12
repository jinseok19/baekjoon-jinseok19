import sys
import random
n_list = []
for i in range(9):
    n_list.append(int(sys.stdin.readline()))
result = 0

while result != 100:
    r_case = random.sample(n_list,7)
    result = sum(r_case)

sorted_case = sorted(r_case)

for i in sorted_case:
    print(i)
