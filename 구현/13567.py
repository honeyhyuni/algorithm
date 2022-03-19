# https://www.acmicpc.net/problem/13567
import sys

n, m = map(int, input().split())
x, y, d = n, 0, 0

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(m):
    order = list(map(str, input().split()))
    if order[0] == "MOVE":
        for _ in range(int(order[1])):
            nx = x + dx[d]
            ny = y + dy[d]
            x, y = nx, ny
        if not(0 <= x < (n+1) and 0 <= y < (n+1)):
            print(-1)
            sys.exit()
    else:
        if order[1] == "0":
            d = (d+1)%4
        else:
            d = (d-1)%4


print(y, abs(x-n))