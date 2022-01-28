# https://www.acmicpc.net/problem/2167
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
k = int(input())

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            result += arr[i][j]
    print(result)