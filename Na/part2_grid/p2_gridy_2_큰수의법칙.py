""" 2021 10 8
    동빈나 part2 탐욕 알고리즘 - 큰 수 법칙
"""
# m번 더하고, k번 까지 연속 가능
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속 가능 횟수 K
# K는 항상 M보다 작거나 같다.

N, M, K = map(int, input().split())
num_list = [int(x) for x in input().split()] # list를 입력으로 int로 받기

num_list.sort() # 2 4 4 5 6

nm_sum = 0
cnt = 0

for i in range(M): # 0-7
    if cnt == K:
        nm_sum += num_list[N-2]
        cnt = 0
        continue
        
    cnt += 1
    nm_sum += num_list[N-1]
    
print(nm_sum)

"""   
<입력>    
5 8 3
2 4 5 4 6

<출력>
46

"""