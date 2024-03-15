import sys
import math

N = int(sys.stdin.readline())
cnt = 0
k = int(math.factorial(N))
str_k = str(k)
for i in str_k[::-1]:
    if i == "0":
        cnt +=1
    else:
        break

print(cnt)