""" 2021 10 18
    동빈나 part3 아이디어 구현 - 게임 개발
"""
# N x M의 맵이 존재
# 캐릭터는 현재 위치에서 왼쪽 방향으로 부터 갈 곳 정함
# 못가본곳이면 왼쪽 방향으로 회전한뒤, 왼쪽 방향으로 전진
# 가본 곳이거나 바다(1) 이면 왼쪽 방향으로만 회전.

N, M = map(int, input().split()) # 맵의 크기 (row, col)
x, y , d = map(int, input().split()) # 캐릭터의 x,y 좌표와 현재 보고 있는 방향

map_list = [] # map의 리스트
dir_list = [0,3,2,1] # 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽  왼쪽으로 이동.
dx = [] # col
dy = [] # row

for i in range(N): # row 만큼 for문
    map_list.append(list( map(int, input().split()) ))
    

    