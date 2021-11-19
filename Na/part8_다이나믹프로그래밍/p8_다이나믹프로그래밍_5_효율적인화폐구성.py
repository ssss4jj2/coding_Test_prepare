""" 2021 10 31
    동빈나 part8 다이나믹프로그래밍 - 효율적인 화폐 구성
"""

N, M = map(int,input().split())
array = []
for i in range(N):
    array.append(int(input()))
    
d = [10001]*(M+1)
d[0] = 0
for i in range(N):
    for j in range(array[i],M+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j -array[i]] + 1)
            