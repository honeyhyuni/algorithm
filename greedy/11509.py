# https://www.acmicpc.net/problem/11509
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if arr[i] == 0:
        continue
    cnt += 1
    H = arr[i]
    arr[i] = 0
    for j in range(i + 1, n):
        if arr[j] == H - 1:
            arr[j] = 0
            H -= 1
        if H == 0:
            continue
print(cnt)
