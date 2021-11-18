""" 2021 10 22
    동빈나 part4 정렬 - 성적이 낮은 순서로 학생 출력하기
"""

# N명의 학생
# 학생정보는 (이름, 성적)
# 성적 낮은 학생순으로 출력

N = int(input())

std_tuple = []
for i in range(N):
    re = input().split( ) # 리스트 저장
    std_tuple.append((re[0], float(re[1])))

std_tuple.sort(key = lambda x: x[1]) # 
# sorted(std_tuple, key = lambda x: int.lower)

print(std_tuple)

for i in range(N):
    print(std_tuple[i][0], end = ' ')

# std_list = []
# for i in range(N):
#     std_list.append(std_tuple[i][0], int(std_tuple[i][1]))
  
# print(std_list)  

# print(std_tuple)
# print(std_tuple[0][1])
# print(type(std_tuple[0][1]))