""" 2021 10 18
    동빈나 part3 아이디어 구현 - 왕실의 나이트
"""
# 나이트는 L 자 모양으로 이동이 가능하다.
# 현재 위치를 입렵 받고, 나이트가 움직일 수 있는 위치의 수를 구함.
# 판의 크기는 8x8 ( col : a~h, row : 1~8 )
# a의 아스키 코드 : 97 ~ h의 아스키 코드 : 104


nP = input() # now position
nP = nP.lower() # input을 소문자로

row  = int(nP[1])  # 10이 넘어가면 1밖에 안됨. 수정!
col = ord(nP[0]) - 96 # a~h를 1부터 8까지로 변환

# print(row, col)
# print(type(row), type(col))

cnt = 0 # count

mP = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)] # move point (row, col) 움직일 수 있는 방향(8)

for i in range(len(mP)):
    new_pos = (row + mP[i][0], col + mP[i][1])
    
    if new_pos[0] >= 1 and new_pos[0] <= 8 and new_pos[1] >= 1 and new_pos[1] <= 8:
        cnt += 1
        
    # new_row = row + mP[i] # 새로운 행
    # new_col = col + mP[i] # 새로운 열
    # if new_row >= 1 and new_row <= 8 and new_col >= 1 and new_col <= 8: # 행렬의 위치가 0이 아닐때 
    #     cnt += 1

print(cnt)