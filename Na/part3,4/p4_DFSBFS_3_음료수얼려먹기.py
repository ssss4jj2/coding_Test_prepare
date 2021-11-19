""" 2021 10 19
    동빈나 part4 DFS/BFS - 음료수 얼려 먹기
"""

# N x M 크기의 얼음틀 존재
# 0은 구멍 뚫려 있는 부분, 1은 칸막이 존재
# 1이 칸막이고, 1로 둘려 쌓여진 0이 얼음이 된다. 그래서 얼음의 갯수 구하기 

N, M = map(int, input().split()) # 맵의 크기 (row, col) 얼음틀

map_list = [] # 얼음 틀

for i in range(N):  # 0 이면 구멍, 1은 칸막이
    map_list.append(list(map(int, input())))
    
# print(N, M)
# print(map_list)

# 상하좌우 순
x_way = [0, 0, -1, 1] # ( x = 열, y = 행 )
y_way = [-1, 1, 0, 0] 

cnt = 0  # 얼음의 갯수를 카운트 0으로 초기화

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return 0
    
    if map_list[x][y] == 0: # 얼음 구멍이라면
        map_list[x][y] = 1 # 1로 변환하여 갔다고 변환

        for i in range(len(x_way)): # 4번의 상하좌우
            new_x = x + x_way[i]
            new_y = y + y_way[i]
            dfs(new_x, new_y) # 재귀 함수
        return 1
    
    # return 0
    
            
for i in range(N):
    for j in range(M):
        if dfs(i , j) == 1:
            cnt += 1
            
print(cnt)