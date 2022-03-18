# https://www.acmicpc.net/problem/21608
import sys
input = sys.stdin.readline
n = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = [[0] * n for i in range(n)]
dic = {}
for k in range(n * n):
    a = list(map(int, input().split()))
    dic[a[0]] = a[1:]
    x, y, fav, zero = 0, 0, -1, -1  # 갱신할 x,y 좌표, 친한친구, 빈칸갯수
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                temp_fav, temp_zero = 0, 0
                for _ in range(4):
                    nx = i + dx[_]
                    ny = j + dy[_]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in dic[a[0]]:
                            temp_fav += 1
                        if arr[nx][ny] == 0:
                            temp_zero += 1
                if temp_fav > fav or (temp_fav == fav and temp_zero > zero):
                    fav, zero = temp_fav, temp_zero
                    x, y = i, j
    arr[x][y] = a[0]
result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for _ in range(4):
            x = i + dx[_]
            y = j + dy[_]
            if 0 <= x < n and 0 <= y < n:
                if arr[x][y] in dic[arr[i][j]]:
                    cnt += 1
        if cnt != 0:
            result += (10 ** (cnt - 1))
print(result)
