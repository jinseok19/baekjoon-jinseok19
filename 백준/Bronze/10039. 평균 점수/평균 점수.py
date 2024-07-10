list_avg = []
for i in range(5):
    a = int(input())
    if a< 40:
        a = 40
    list_avg.append(a)

print(sum(list_avg)//5)
    

