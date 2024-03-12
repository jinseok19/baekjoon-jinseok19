import sys

N = int(sys.stdin.readline())
result = 0
for i in range(1, N+1):
    N_sum = sum(map(int, str(i)))
    result = N_sum + int(i)

    if result == N:
        print(i)
        break
    elif i == N:
        print(0)
