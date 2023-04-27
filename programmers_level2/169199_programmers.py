# https://school.programmers.co.kr/learn/courses/30/lessons/169199
from collections import deque


def solution(board):
    n, m = len(board), len(board[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    visited = [[-1] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                q.append((i, j, 0))
                visited[i][j] = 0

    while q:
        x, y, c = q.popleft()
        if board[x][y] == 'G':
            return c
        for _ in range(4):
            for __ in range(1, max(n, m)+1):
                nx = x + dx[_] * __
                ny = y + dy[_] * __
                if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] == 'D':
                    xx = nx-dx[_]
                    yy = ny-dy[_]
                    if visited[xx][yy] == -1:
                        visited[xx][yy] = c + 1
                        q.append((xx, yy, c + 1))
                    break
    return -1


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
