""" 2021 10 27
    동빈나 part9 최단경로 - 미래 도시
"""
# 1~N번의 회사 - 특정 회사끼리는 서로 도로로 연결
# A는 현재 1번 회사 위치 X 번 회사 방문
# 한번 움직이는데 1만큼의 시간
# 소개팅 상대는 K번 회사 X번 회사 가기전 들림 1->K->X번 회사 
# 전체 회사의 개수 N, 경로의 개수 M (1<=N,M<=100)
# 도착 회사 X번, 소개팅 K번 회사 (1<=K<=100)

N, M = map(int, input().split())

path_list = []
for i in range(M):
    re = input().split()   
    path_list.append((int(re[0]), int(re[1])))    

X, K = map(int, input().split())

# print(path_list)
