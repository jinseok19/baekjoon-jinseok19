import sys

N = int(sys.stdin.readline())
name = []
result =[]
for i in range(N):
    name.append((sys.stdin.readline().rstrip())[0])

for i in set(name):
    if name.count(i)>=5:
        result.append(i)
    
sorted_result = sorted(result)
if len(sorted_result)==0:
    print("PREDAJA")
else:
    for i in sorted_result:
        print(i,end="")
