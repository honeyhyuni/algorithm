# https://www.acmicpc.net/problem/5014
from collections import deque
f, s, g, u, d = map(int, input().split())

dx = [u, -d]

arr = [-1] * f

arr[s-1] = 0

q = deque()
q.append(s-1)
while q:
    x = q.popleft()
    for _ in range(2):
        nx = x + dx[_]
        if 0 <= nx < f and arr[nx] == -1:
            arr[nx] = arr[x] + 1
            q.append(nx)

if arr[g-1] == -1:
    print("use the stairs")
else:
    print(arr[g-1])