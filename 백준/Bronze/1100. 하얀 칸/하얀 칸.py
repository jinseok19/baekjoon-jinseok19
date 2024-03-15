import sys
chase = []
result = 0
for i in range(8):
    chase.append(sys.stdin.readline().rstrip())

for i in range(8):
    for j in range(8):
        if (i+j) %2 ==0:
            if chase[i][j] == "F":
                result +=1
print(result)