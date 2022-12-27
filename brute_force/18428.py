# https://www.acmicpc.net/problem/18428
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(str, input().split())) for i in range(n)]

teacher = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "T":
            teacher.append((i, j))

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
ans = "NO"


def check():
    for i, j in teacher:
        for _ in range(4):
            for __ in range(n):
                nx = i + dx[_] * __
                ny = j + dy[_] * __
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == "S":
                        return False
                    elif arr[nx][ny] == "O":
                        break
                else:
                    break
    return True


def back(x, cnt):
    global ans
    if cnt == 3:
        if check():
            ans = "YES"
        return
    for i in range(x, n):
        for j in range(n):
            if arr[i][j] == "X":
                arr[i][j] = "O"
                back(i, cnt + 1)
                arr[i][j] = "X"


back(0, 0)
print(ans)