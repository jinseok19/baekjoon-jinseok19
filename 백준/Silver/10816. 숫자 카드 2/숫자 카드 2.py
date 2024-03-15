import sys
N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))

count = {}

for card in N_list:
    if card in count:
        count[card] +=1
    else:
        count[card] = 1

for t in M_list:
    result = count.get(t)

    if result == None:
        print(0, end = " ")
    else:
        print(result, end = " ")
        