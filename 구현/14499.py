# https://www.acmicpc.net/problem/14499
import sys

input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
k_arr = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def ch(i):
    if i == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif i == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif i == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif i == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


for i in k_arr:
    nx = x + dx[i]
    ny = y + dy[i]
    if not (0 <= nx < n and 0 <= ny < m):
        continue
    ch(i)
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[1]
    else:
        dice[1] = arr[nx][ny]
        arr[nx][ny] = 0
    x = nx
    y = ny
    print(dice[6])
