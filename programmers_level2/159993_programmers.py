# https://school.programmers.co.kr/learn/courses/30/lessons/159993
from collections import deque


def solution(maps):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])
    visited = [[[-1] * 2 for i in range(m)] for i in range(n)]
    q = deque()
    bol = False
    for i in range(n):
        if bol:
            break
        for j in range(m):
            if maps[i][j] == 'S':
                q.append((i, j, 0))
                visited[i][j][0] = 0
                bol = True
                break
    while q:
        x, y, l = q.popleft()
        if l == 1 and maps[x][y] == "E":
            return visited[x][y][l]
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][l] == -1 and maps[nx][ny] != "X":
                if maps[nx][ny] == "L":
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][l] + 1
                else:
                    q.append((nx, ny, l))
                    visited[nx][ny][l] = visited[x][y][l] + 1
    return -1


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))