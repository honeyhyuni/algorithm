# https://www.acmicpc.net/problem/10836
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[1] * n for i in range(n)]
grow = [0] * (2*n-1)
for i in range(m):
    a, b, c = map(int, input().split())
    for j in range(a, a+b):
        grow[j] += 1
    for j in range(a+b, 2*n-1):
        grow[j] += 2
idx = 0
for i in range(n-1, -1, -1):
    arr[i][0] += grow[idx]
    idx += 1
for i in range(1, n):
    arr[0][i] += grow[idx]
    idx += 1

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] += arr[0][j] - 1
for i in arr:
    print(*i)