""" 2021 10 27
    동빈나 part7 이진탐색 - 떡볶이 떡 먹기
"""

# 떡의 총 길이에 맞춰 자른다.
# 높이 H 보다 크면 자르고, 짧으면 짜르지 않는다.
# H보다 큰 것을 짜를때 남는 것의 합이 M이 되는 최대 H 값


N, M = map(int,input().split())
array = list(map(int, input().split()))
# array = sorted(array)

H = 0 # 높이 값 초기화
start = 0 
end = max(array)

while start <= end:
    sum_M = 0
    mid = (start + end) // 2 # // 정수부분만 사용
    
    for x in array:
        if x > mid:
            sum_M += (x - mid)
    
    if sum_M < M:
        end = mid - 1
    else:
        H = mid
        start = mid + 1


print(H)
            
    
    
