# https://www.acmicpc.net/problem/2110
import sys

input = sys.stdin.readline
n, c = map(int, input().split())
arr = [int(input()) for i in range(n)]
arr.sort()
result = []

start, end = 1, arr[-1] - arr[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    now = arr[0]
    for i in arr:
        if now + mid <= i:
            cnt += 1
            now = i
    if cnt >= c:
        start = mid + 1
        result.append(mid)
    else:
        end = mid - 1
print(max(result))
