# https://www.acmicpc.net/problem/1939
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]


def bfs(v):
    visited = [False] * (n + 1)
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        x = q.popleft()
        if x == e:
            return True
        for _, __ in arr[x]:
            if not visited[_] and v <= __:
                visited[_] = True
                q.append(_)
    return False


temp = 0
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
    temp = max(temp, c)
s, e = map(int, input().split())

left, right = 0, temp
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)