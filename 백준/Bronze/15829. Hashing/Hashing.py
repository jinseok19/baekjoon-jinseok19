import sys

n = int(sys.stdin.readline())
M = 1234567891
R = 31
string = sys.stdin.readline().rstrip()

result = 0

for i in range(len(string)):
    num = ord(string[i])-96
    result += num * (R**i)

print(result %M)