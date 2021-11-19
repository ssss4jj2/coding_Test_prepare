""" 2021 10 25
    동빈나 part7 이진탐색 - 부품 찾기
"""
# 첫째 줄은 부품 N개
# 셋째 줄은 손님 M개
# 손님이 원하는 부품 중에 가게에 있으면 yes 없으면 no

# import sys

def binary_search(array, target, start, end): # 이진 탐색
    if start > end:
        return None
    
    while start <= end:
        mid = (start + end) // 2 # 배열의 중간값
        
        if array[mid] == target:
            return mid
        elif array[mid] > target: # 배열의 중간값이 타겟보다 클경우
            # mid = (start + mid) / 2 # 새로운 중앙값 생성
            # return binary_search(array, target, start, mid - 1)
            end = mid - 1
        else: # 배열의 중간값이 타겟보다 작을 경우
            # return binary_search(array, target, mid + 1, end)
            start = mid + 1
    return None
    

N = int(input()) # 가게의 부품 개수
array1 = list(map(int, input().split())) # 가게가 가지고 있는 부품 번호
array1 = sorted(array1)
# print(array1)

M = int(input()) # 손님이 원하는 부품 개수
array2 = list(map(int, input().split())) # 손님이 원하는 부품 번호  즉 target이 된다
array2 = sorted(array2)
# print(array2)

for i in range(M):
    target = array2[i]
    rlt = binary_search(array1, target, 0, N-1) # 이진탐색을 한 결과
    if rlt == None:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')
    