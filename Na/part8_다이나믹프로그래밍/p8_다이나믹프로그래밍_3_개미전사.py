""" 2021 10 31
    동빈나 part8 다이나믹프로그래밍 - 개미전사
"""

# 들키지 않으려면 최소 한칸 띄우고 털어야함
# 일직선상 창고중 최대로 털어야함
# 첫째 줄에는 창고 개수 N
# 둘째 줄에는 공백으로 각 창고에 식량 개수 

N = int(input())
food_map = list(map(int,input().split()))

d = [0] * (N + 1)

"""bottom up"""
d[0] = food_map[0] # 하나 일때는 하나가 최대임
d[1] = max(food_map[0], food_map[1]) # 두개일 때는 둘 중에 최대임

for i in range(2,N): # 2부터 N-1개 까지(즉 3개 이상일 때)
    d[i] = max(d[i-1],d[i-2] + food_map[i])
    
print(d[N-1])
     