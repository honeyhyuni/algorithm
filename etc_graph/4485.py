# https://www.acmicpc.net/problem/4485
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
index = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    dp = [[INF] * n for i in range(n)]
    for i in range(n):
        arr.append(list(map(int, input().split())))
    heap = []
    dp[0][0] = arr[0][0]
    heappush(heap, [dp[0][0], 0, 0])
    while heap:
        dist, x, y = heappop(heap)
        if dp[x][y] < dist:
            continue
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + arr[nx][ny]
                if dp[nx][ny] > cost:
                    dp[nx][ny] = cost
                    heappush(heap, [cost, nx, ny])
    print("Problem " + str(index) +": " + str(dp[n-1][n-1]))
    index += 1


