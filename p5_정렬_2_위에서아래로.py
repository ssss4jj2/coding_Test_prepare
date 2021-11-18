""" 2021 10 22
    동빈나 part4 정렬 - 위에서 아래로
"""

# 하나의 수열에 다양한 수가 존재. 이 수를 크기에 맞게 정렬하라 
# 내림차순으로 
import time
start_time = time.time()

N = int(input()) # 수열 안에 수의 갯수

num_list = []
for i in range(N):
    num_list.append(int(input()))
# print(num_list)

start_time = time.time()

num_list.sort()  # 내림차순으로 sort,  오름차순으로 하려면 sort(reverse=True)

for i in range(N):
    print(num_list[i], end = ' ')
    
end_time = time.time()

print("time : ", end_time - start_time) # 수행 시간 출력
    