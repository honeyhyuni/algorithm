# https://programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(places):
    answer = []
    for qwe in places:
        arr = qwe
        result = 0
        for i in range(5):
            for j in range(5):
                if arr[i][j] == "P":
                    result += bfs(i, j, arr)
        if result > 0:
            answer.append(0)
        else:
            answer.append(1)
    return answer


def bfs(i, j, arr):
    q = deque()
    q.append([i, j, 0])
    visited = [[False] * 5 for i in range(5)]
    visited[i][j] = True
    while q:
        x, y, cnt = q.popleft()
        if cnt == 3:
            return 0
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and arr[nx][ny] != "X":
                if arr[nx][ny] == "O":
                    visited[nx][ny] = True
                    q.append([nx, ny, cnt + 1])
                else:
                    temp = abs(nx - i) + abs(ny - j)
                    if temp <= 2:
                        return 1
    return 0


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
