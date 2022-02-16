# https://www.acmicpc.net/problem/1021
from collections import deque

n, m = map(int, input().split())
lst = list(map(int, input().split()))
q = deque([x for x in range(1, n + 1)])
cnt = 0

for num in lst:
    if q.index(num) <= len(q) // 2:
        while q[0] != num: # 왼쪽으로 한바퀴이동
            q.rotate(-1)
            cnt += 1
    else:
        while q[0] != num: # 오른쪽으로 한바퀴이동
            q.rotate(1)
            cnt += 1
    q.popleft()
print(cnt)
