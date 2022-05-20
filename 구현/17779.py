# https://www.acmicpc.net/problem/17779
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
lst = [[i, j] for i in range(1, n // 2 + 1) for j in range(1, n // 2 + 1)]  # d1, d2 배열
result = sys.maxsize


#  5선거구 테두리 잡기
def check(x, y):
    global result
    xx, yy = x, y
    for d1, d2 in lst:
        visited = [[0] * n for i in range(n)]
        bol = False
        for i in range(d1):
            if x + 1 < n and y + 1 < n:
                x += 1
                y += 1
                visited[x][y] = 5
            else:
                bol = True
                break
        for i in range(d2):
            if x + 1 < n and 0 <= y - 1:
                x += 1
                y -= 1
                visited[x][y] = 5
            else:
                bol = True
                break
        for i in range(d1):
            if 0 <= x - 1 and 0 <= y - 1:
                x -= 1
                y -= 1
                visited[x][y] = 5
            else:
                bol = True
                break
        for i in range(d2):
            if 0 <= x - 1 and y + 1 < n:
                x -= 1
                y += 1
                visited[x][y] = 5
            else:
                bol = True
                break
        x, y = xx, yy
        if not bol:
            result = min(result, divide(d1, d2, visited, xx, yy))


# 5 구역 모두 나눠줌
def divide(d1, d2, visited, x, y):
    for i in range(n):
        s, e, cnt = 0, 0, 0
        for j in range(n):
            if visited[i][j] == 5:
                if cnt == 0:
                    s = j
                    cnt += 1
                else:
                    e = j
                    cnt += 1
            if i < x + d2 and j <= y and visited[i][j] == 0:
                visited[i][j] = 1
            elif i <= x + d1 and y < j < n and visited[i][j] == 0:
                visited[i][j] = 2
            elif x + d2 <= i < n and j < y - d2 + d1 and visited[i][j] == 0:
                visited[i][j] = 3
            else:
                if visited[i][j] == 0:
                    visited[i][j] = 4
        if cnt == 2:
            for j in range(s, e + 1):
                visited[i][j] = 5
    return min_v(visited)


# 최소값 구해줌
def min_v(visited):
    ans = [0] * 5
    for i in range(n):
        for j in range(n):
            ans[visited[i][j] - 1] += arr[i][j]

    return max(ans) - min(ans)


for i in range(n):
    for j in range(1, n):
        check(i, j)

print(result)
