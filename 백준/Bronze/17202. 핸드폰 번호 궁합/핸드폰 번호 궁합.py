import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
result = ''

for i in range(len(a)):
    result += a[i] + b[i]


while(len(result)> 2):
    tmp = ''

    for j in range(0,len(result)-1):
        tmp += str(int(result[j]) + int(result[j+1]))[-1]

    
    result = tmp

    

print(result)