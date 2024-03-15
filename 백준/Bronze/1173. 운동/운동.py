import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())
time = total = 0
purse = m

if m + T > M:
    print(-1)
else:
    while time < N:
        if purse + T <= M:
            purse += T
            time += 1
            total += 1
        else:
            purse -= R
            if purse < m:
                purse = m
            total += 1
    print(total)
        