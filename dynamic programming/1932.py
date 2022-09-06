# https://www.acmicpc.net/problem/1932
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

for i in range(1, n):
    for j in range(len(arr[i])):
        temp = 0
        for k in [j-1, j]:
            if 0 <= k < len(arr[i-1]):
                temp = max(temp, arr[i-1][k])
        arr[i][j] += temp
print(max(arr[-1]))
