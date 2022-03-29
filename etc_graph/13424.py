# https://www.acmicpc.net/problem/13424
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    INF = sys.maxsize
    result, index = INF, 0
    arr = [[INF] * (n + 1) for i in range(n + 1)]
    for i in range(m):
        x, y, z = map(int, input().split())
        arr[x][y] = z
        arr[y][x] = z
    k = int(input())
    friend = list(map(int, input().split()))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                arr[i][j] = 0
    for q in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if arr[a][b] > arr[a][q] + arr[q][b]:
                    arr[a][b] = arr[a][q] + arr[q][b]

    for i in range(1, n + 1):
        total = 0
        for f in friend:
            total += arr[f][i]
        if result > total :
            index = i
            result = total
    print(index)






