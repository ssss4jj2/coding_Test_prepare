""" 2021 10 22
    동빈나 part4 정렬 - 두 배열의 원소 교체
"""
# 두개의 배열 A,B 
# 두 배열은 N개의 원소로 구성, 배열의 구성은 모두 자연수
# K번 바꿔치기, A와 B 서로 바꿈
# 목표는 A 모든 원소의 합이 최대
# A의 모든 원소 합 출력

N, K = map(int, input().split())

A_list = [] # 리스트 초기화
B_list = []

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
print(A_list, B_list)

A_list.sort() # 오름차순을 정렬
B_list.sort() 
print(A_list, B_list)

for i in range(K):
    if A_list[i] < B_list[(N-1) - i]: # A의 원소가 B의 원소 보다 작은경우만
        A_list[i], B_list[(N-1) - i] = B_list[(N-1) - i] , A_list[i]

print(A_list, B_list)
print(sum(A_list))