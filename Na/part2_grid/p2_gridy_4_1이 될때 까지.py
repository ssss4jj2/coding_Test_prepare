""" 2021 10 10
    동빈나 part2 탐욕 알고리즘 - 1이 될 때까지
"""

## N에서 1을 뺀다.
## N에서 K로 나눈다.
## N은 항상 K 보다 크거나 같다.

N, K = map(int, input().split())

n = N
kd = K
cnt = 0 # 횟수

while True:
    if n == 1:
        break
    else:
        if n % kd == 0: # 나머지가 0일때
            n = n/kd
            cnt += 1
        
        else: # 나머지가 0이 아닐때
            n -= 1
            cnt += 1
        
print(cnt)


# n, k = map(int, input().split())

# result = 0

# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#     # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1
#     n //= k

# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n - 1)
# print(result)