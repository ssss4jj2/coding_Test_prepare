""" 2021 10 31
    동빈나 part8 다이나믹프로그래밍 - 바닥공사
"""
# 가로가 N, 세로는 2인 바닥
# 바닥을 채울수 있는 경우의 수를 구함
# 최대로 채울수 있는 방법의 수를 796,796으로 나눈 나머지를 출력

N = int(input())
d = [0] * (N+1) # 결과를 저장하기 위함

d[0] = 1 # 2X1의 타일은 2X1 밖에 없다
d[1] = 3 # 2X2는 세개

for i in range(2,N):
    d[i] = (d[i - 1] + d[i - 2]* 2) % 796796

print(d[N-1])
    
