""" 2021 10 8
    동빈나 part2 탐욕 알고리즘 - 숫자 카드 게임
"""
# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
# 카드는 N x M 형태 , N 은 행 M 은 열

N, M = map(int, input().split())

n_list = []
# card_list = []

c_max = 0 # 가장 작은 수 중에서의 최대 
c_2_min = 0 # 리스트 하나당 최소 

for i in range(N): # 행의 횟수 만큼 반복
    n_list = [int(x) for x in input().split()] # list를 입력으로 int로 받기
    
    c_2_min = 10001 # 숫자는 최대 10000이기 때문에
    
    # for x in n_list:
    #     c_2_min = min(c_2_min,x)
    
    for j in range(len(n_list)):
        if c_2_min > n_list[j]:
            c_2_min = n_list[j]
        
    c_max = max(c_max, c_2_min)

print(c_max)
    