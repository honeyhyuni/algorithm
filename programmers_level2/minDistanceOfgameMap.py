# https://programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        if x == len(maps) - 1 and y == len(maps[0])-1:
            return maps[x][y]
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append([nx, ny])

    return -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
