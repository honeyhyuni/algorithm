# https://www.acmicpc.net/problem/3190
import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


input = sys.stdin.readline
n = int(input())
k = int(input())
arr = [[0] * n for i in range(n)]
for i in range(k):
    k1, k2 = map(int, input().split())
    arr[k1 - 1][k2 - 1] = 2
l = int(input())

q = deque()
q.append((0, 0))
arr[0][0] = 1
l_list = {}
for i in range(l):
    X, C = input().split()
    l_list[int(X)] = C

cnt = 0
d = 0
while True:
    if cnt in l_list.keys():
        if l_list[cnt] == "D":
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
    x, y = q[-1]
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] == 1:
        cnt += 1
        break
    if arr[nx][ny] == 2:
        q.append((nx, ny))
        arr[nx][ny] = 1
    elif arr[nx][ny] == 0:
        q.append((nx, ny))
        arr[nx][ny] = 1
        xx, yy = q.popleft()
        arr[xx][yy] = 0
    cnt += 1
print(cnt)