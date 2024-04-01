import sys
e = ['a','e','i','o','u','A','E','I','O','U']

while True:
    cnt = 0
    string = sys.stdin.readline().rstrip()
    if string =='#':
        break
    else:
        for i in string:
            if i in e:
                cnt +=1
        
    print(cnt)