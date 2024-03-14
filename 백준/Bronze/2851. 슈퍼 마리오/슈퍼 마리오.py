import sys
n_list = []
for i in range(10):
    n_list.append(int(sys.stdin.readline()))
result = 0
res_min = 10000000
for i in n_list:
    result +=i
    res = abs(100-result)
    if res <= res_min:
        res_min = res
        r_result = result

print(r_result)
