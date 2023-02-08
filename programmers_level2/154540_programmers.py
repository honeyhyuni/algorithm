# https://school.programmers.co.kr/learn/courses/30/lessons/154540
from collections import deque


def solution(maps):
    answer = []
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and not visited[i][j]:
                visited[i][j] = True
                q = deque()
                q.append((i, j))
                sum_ = int(maps[i][j])
                while q:
                    x, y = q.popleft()
                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X":
                            visited[nx][ny] = True
                            sum_ += int(maps[nx][ny])
                            q.append((nx, ny))
                answer.append(sum_)
    return sorted(answer) if answer else [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
print(solution(["XXX", "XXX", "XXX"]))
