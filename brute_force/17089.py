# https://www.acmicpc.net/problem/17089
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
visited = [[False] * (n + 1) for i in range(n + 1)]
arr = [0] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    visited[x][y], visited[y][x] = True, True
    arr[x] += 1
    arr[y] += 1

result = sys.maxsize

for a in range(1, n + 1):
    if arr[a] < 2:
        continue
    for b in range(a + 1, n + 1):
        if not visited[a][b] or arr[b] < 2:
            continue
        for c in range(b + 1, n+1):
            if not visited[a][c] or not visited[b][c] or arr[c] < 2:
                continue
            result = min(result, arr[a]+arr[b]+arr[c] - 6)
print(result if result != sys.maxsize else -1)
