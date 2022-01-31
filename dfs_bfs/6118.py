# https://www.acmicpc.net/problem/6118
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
visited = [-1] * (n+1)
arr = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y) # 양방향
    arr[y].append(x)

visited[1] = 0
q = deque()
q.append(1)
cnt = 0
while q:
    x_ = q.popleft()
    cnt += 1
    for i in arr[x_]:
        if visited[i] == -1:
            visited[i] = visited[x_] + 1 # 연결 크기 마다 1씩 증가
            q.append(i)

x = max(visited)
print(visited.index(x), end=' ')
print(x, end=' ')
print(visited.count(x))