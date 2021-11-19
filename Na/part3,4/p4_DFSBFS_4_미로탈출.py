""" 2021 10 19
    동빈나 part4 DFS/BFS - 미로 탈출
"""

# N x M 직사각형 미로
# 처음의 위치 (1,1) 출구는 (N,M)
# 괴물 = 0, 괴물 X = 1
# 움직이기 위한 최소 칸의 개수 = 출력

from collections import deque  # list를 사용하여 append 와 pop을 해주게 되면 시간복잡도가  O(n)이 되어 커진다.

N, M = map(int, input().split())

map_list = []
for i in range(N):
    map_list.append(list(map(int, input())))
    
# 상하좌우 순
dx = [0, 0, -1, 1] # ( x = 열, y = 행 )
dy = [-1, 1, 0, 0] 

def bfs(x, y):
    q = deque() # 데크를 이용해 큐 생성
    q.append((x, y)) # (x,y) append
    print("q = ",q)
    
    while q: # q가 빌때 까지 
        (x, y) = q.popleft() # 큐의 제일 왼쪽을 삭제하고 그 값을 리턴
        
        print (q)
        print("popleft = ",(x,y))
        
        for i in range(len(dx)): # 4가지 방향 (상하좌우 순)
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if new_x <= -1 or new_x >= N or new_y <= -1 or new_y >= M: # 새 좌표가 밖으로 나갈때 
                continue
            
            if map_list[new_x][new_y] == 0: # 새 좌표의 방문한 노드가 괴물이 있을 때 무시.
                continue 
            
            if map_list[new_x][new_y] == 1: # 방문한 노드가 괴물이 없을때
                map_list[new_x][new_y] = map_list[x][y] + 1 # 방문했다고 +1을 해줌  count 세는 거임
                q.append((new_x, new_y)) # 새로운 좌표를 큐에 넣음
    return   map_list[new_x - 1][new_y - 1]
                
print(bfs(0,0))            