# https://www.acmicpc.net/problem/1719
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
INF = sys.maxsize
arr = [[INF] * (n + 1) for i in range(n + 1)]  # 최단경로 크기 배열
result = [[0] * (n + 1) for i in range(n + 1)]  # 다음경로 배열

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    arr[b][a] = c
    result[a][b] = b
    result[b][a] = a

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            arr[i][j] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if arr[a][b] > arr[a][k] + arr[k][b]:  
                arr[a][b] = arr[a][k] + arr[k][b] # 최단경로 최신화
                result[a][b] = result[a][k]  # 바로 다음 노드로 변경

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if result[i][j] == 0:
            print("-", end=' ')
        else:
            print(result[i][j], end=' ')
    print()
