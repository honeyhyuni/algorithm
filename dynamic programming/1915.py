# https://www.acmicpc.net/problem/1915
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip())))

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            arr[i][j] = min(arr[i][j-1], arr[i-1][j], arr[i-1][j-1]) + 1

print(max(map(max, arr)) ** 2)