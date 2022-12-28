# https://www.acmicpc.net/problem/18430
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

dd = [[0, -1, 1, 0], [0, -1, -1, 0], [-1, 0, 0, 1], [0, 1, 1, 0]]
visited = [[False] * m for _ in range(n)]
ans = 0


def back(x, y, c):
    global ans
    if y == m:
        y = 0
        x += 1
    if x == n:
        ans = max(ans, c)
        return
    if not visited[x][y]:
        visited[x][y] = True
        for x1, y1, x2, y2 in dd:
            nx1 = x + x1
            ny1 = y + y1
            nx2 = x + x2
            ny2 = y + y2
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m and not visited[nx1][ny1] and not \
                    visited[nx2][ny2]:
                visited[nx1][ny1] = visited[nx2][ny2] = True
                back(x, y + 1, c + (arr[x][y] * 2 + arr[nx1][ny1] + arr[nx2][ny2]))
                visited[nx1][ny1] = visited[nx2][ny2] = False
        visited[x][y] = False
    back(x, y + 1, c)


for i in range(n):
    for j in range(m):
        back(i, j, 0)

print(ans)
