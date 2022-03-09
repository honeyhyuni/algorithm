# https://www.acmicpc.net/problem/24446
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

result = [-1] * (n+1)
q = deque()
q.append(r)
visited[r] = True
result[r] = 0

while q:
    x = q.popleft()
    for i in arr[x]:
        if not visited[i]:
            visited[i] = True
            result[i] = result[x] + 1  # 부모노드 크기보다 1 증가
            q.append(i)

print("\n".join(map(str, result[1:])))

