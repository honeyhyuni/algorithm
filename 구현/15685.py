# https://www.acmicpc.net/problem/15685
import sys
input = sys.stdin.readline
n = int(input())
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
arr = [[0] * 101 for i in range(101)]
for ii in range(n):
    y, x, d, g = map(int, input().split())
    arr[x][y] = 1
    q = [d]
    dd = [d]
    for i in range(g+1):
        for _ in q:
            x += dx[_]
            y += dy[_]
            arr[x][y] = 1
        q = [(i+1) % 4 for i in dd]
        q.reverse()
        dd += q

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] == 1:
            result += 1
print(result)