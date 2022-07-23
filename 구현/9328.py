# https://www.acmicpc.net/problem/9328
import sys
from collections import defaultdict, deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
T = int(input())


def bfs():
    global ans
    q = deque()
    for i, j in start:
        visited[i][j] = True
        q.append((i, j))
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] != '*':
                if arr[nx][ny].islower():
                    if arr[nx][ny].upper() in door:
                        for i, j in door[arr[nx][ny].upper()]:
                            arr[i][j] = '.'
                            if (i == 0 or i == n - 1) or (j == 0 or j == m - 1):
                                start.append((i, j))
                    arr[nx][ny] = '.'
                    return True
                elif arr[nx][ny] == '$':
                    ans += 1
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    arr[nx][ny] = '.'
                elif arr[nx][ny] == '.':
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return False


for t in range(T):
    n, m = map(int, input().split())
    arr = [list(map(str, input().rstrip())) for i in range(n)]
    key = list(map(str, input().rstrip()))
    start = []
    door = defaultdict(list)
    ans = 0

    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n - 1) or (j == 0 or j == m - 1):
                if arr[i][j] != '*':
                    if arr[i][j] == '.':
                        start.append((i, j))
                    elif arr[i][j].islower():
                        key.append(arr[i][j])
                        arr[i][j] = '.'
                        start.append((i, j))
                    elif arr[i][j] == '$':
                        ans += 1
                        arr[i][j] = '.'
                        start.append((i, j))
                    elif arr[i][j].isupper():
                        if arr[i][j].lower() in key:
                            start.append((i, j))
                            arr[i][j] = '.'
            if arr[i][j].isupper():
                door[arr[i][j]].append((i, j))
                if arr[i][j].lower() in key:
                    arr[i][j] = '.'

            if arr[i][j].islower():
                if arr[i][j] in key:
                    arr[i][j] = '.'
    for i in key:
        if i.upper() in door.keys():
            for x, y in door[i.upper()]:
                arr[x][y] = '.'

    while True:
        visited = [[False] * m for i in range(n)]
        if not bfs():
            break
    print(ans)
