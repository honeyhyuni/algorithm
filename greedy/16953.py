# https://www.acmicpc.net/problem/16953
from collections import deque
a, b = map(int, input().split())

q = deque()
q.append([a, 1])

result = -1
while q:
    x, y = q.popleft()
    if x == b:
        result = y
        break
    if x * 2 <= b:
        q.append([x * 2, y + 1])
    if int(str(x) + "1") <= b:
        q.append([int(str(x) + "1"), y + 1])

print(result)