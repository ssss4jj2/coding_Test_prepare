from collections import deque  # list를 사용하여 append 와 pop을 해주게 되면 시간복잡도가  O(n)이 되어 커진다.

q=deque()

q.append(0)
print(q)
q.append(1)
print(q)
q.append(2)
print(q)
while q:
    x=q.popleft()
    print(x)



# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111