# https://www.acmicpc.net/problem/16928
import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())

arr = [0] * 101
visited = [-1] * 101
for i in range(n+m):
    x, y = map(int, input().split())
    arr[x] = y

q = deque()
q.append(1)
visited[1] = 0
while q:
    x = q.popleft()
    if x == 100:
        break
    for _ in range(1, 7):
        nx = x + _
        if 0 <= nx < 101 and visited[nx] == -1:
            if arr[nx]:
                nx = arr[nx]
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)

print(visited[100])
