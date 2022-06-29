# https://www.acmicpc.net/problem/13913
from collections import deque

n, k = map(int, input().split())
q = deque()
visited = [False] * 100001
visited[n] = True
q.append((n, 0))
check = [-1] * len(visited)

result = []

while q:
    x, cnt = q.popleft()
    if x == k:
        print(cnt)
        result.append(x)
        while x != -1:
            result.append(check[x])
            x = check[x]
        print(*result[::-1][1:])
        break
    for xx in [x + 1, x - 1, x * 2]:
        if 0 <= xx < len(visited) and not visited[xx]:
            visited[xx] = True
            check[xx] = x
            q.append((xx, cnt+1))
