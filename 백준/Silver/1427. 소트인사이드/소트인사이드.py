import sys
x_list = []
x = str(sys.stdin.readline().rstrip())
for i in x:
    x_list.append(int(i))

sort_list = sorted(x_list, key = lambda  x :-x)
for i in sort_list:
    print(i, end= "")