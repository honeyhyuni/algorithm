# https://www.acmicpc.net/problem/25395
import sys
from collections import deque
input = sys.stdin.readline
n, S = map(int, input().split())
t = list(map(int, input().split()))
h = list(map(int, input().split()))
arr = [(0, 0, 0)]
cnt = 0
for i, j in zip(t, h):
    cnt += 1
    arr.append((i, j, cnt))

visited = [False] * (n+1)
visited[S] = True
q = deque()
q.append(arr[S])
result = []

while q:
    x, y, c = q.popleft()
    result.append(c)
    l_v, r_v = x - y, x + y
    left, right = c-1, c+1
    while 1 <= left:
        if arr[left][0] >= l_v:
            if not visited[left]:
                q.append(arr[left])
                visited[left] = True
            left -= 1
        else:
            break
    while right < (n+1):
        if arr[right][0] <= r_v:
            if not visited[right]:
                q.append(arr[right])
                visited[right] = True
            right += 1
        else:
            break

print(*sorted(result))