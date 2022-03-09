# https://www.acmicpc.net/problem/24447
import sys
from collections import deque
input = sys.stdin.readline
n, m, r = map(int, input().split())
arr = [[] for i in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

for i in arr:
    i.sort()

cnt = 1
result = [-1] * (n+1)
result2 = [0] * (n+1)
q = deque()
q.append(r)
visited[r] = True
result[r], result2[r] = 0, cnt

while q:
    x = q.popleft()
    for i in arr[x]:
        if not visited[i]:
            cnt += 1
            visited[i] = True
            result[i] = result[x] + 1
            result2[i] = cnt
            q.append(i)
rr = 0
for i, j in zip(result, result2):
    rr += (i * j)
print(rr)
