import sys

a, b, v = map(int,sys.stdin.readline().split())

x = (v-b) / (a-b)

if x == int(x):
    print(int(x))
else:
    print(int(x)+1)