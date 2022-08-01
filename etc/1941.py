# https://www.acmicpc.net/problem/1941
import sys

input = sys.stdin.readline
arr = [list(map(str, input().rstrip())) for i in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = set()


def back(temp, S, Y):
    if Y >= 4:
        return
    if len(temp) == 7 and S >= 4:
        result.add(tuple(sorted(temp)))
        return
    club = []
    for x, y in temp:
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in temp:
                club.append((nx, ny))
    for i, j in club:
        if arr[i][j] == "S":
            back(temp + [(i, j)], S + 1, Y)
        else:
            back(temp + [(i, j)], S, Y + 1)


for i in range(5):
    for j in range(5):
        if arr[i][j] == "S":
            back([(i, j)], 1, 0)
print(len(result))
