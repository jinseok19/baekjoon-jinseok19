# import sys

# N = int(sys.stdin.readline().rstrip())
# n_list = ['3','6','9']
# result = 0

# for i in range(1,N+1):
#     str_i = str(i)
#     for j in str_i:
#         if j in n_list:
#             result+=1

# print(result)

#문자열은 문자의 배열
#인덱스를 쓸 수 있다
#리스트 처럼 쓸 수 있다
#문자열은 순서가 있다

#pypy3는 메모리를 더 많이 먹는 대신 
#시간을 적게 쓰는 파이썬의 종류
#그래서 내 코드가 멀쩡한데
#시간초과가 뜬다? -> pypy3로 해보십쇼

import sys

N = int(sys.stdin.readline())
result = 0
for i in range(1, 501):
    for j in range(1, 501):
        if i**2 - j**2 == N:
            result +=1

print(result)
