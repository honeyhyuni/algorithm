# https://www.acmicpc.net/problem/24444
# bfs 이론 문제
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

result = [0] * (n+1)
q = deque()
q.append(r)
visited[r] = True
cnt = 1
result[r] = cnt

while q:
    x = q.popleft()
    for i in arr[x]:
        if not visited[i]:
            q.append(i)
            visited[i] = True
            cnt += 1
            result[i] = cnt

print("\n".join(map(str, result[1:])))
