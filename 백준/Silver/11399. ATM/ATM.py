import sys

n = int(sys.stdin.readline())

atm = list(map(int,sys.stdin.readline().split()))

sorted_atm = sorted(atm)
atm_time = 0
for i in range(1,n+1):
    atm_time += sum(sorted_atm[:i])
print(atm_time)