# https://www.acmicpc.net/problem/1068
import sys

input = sys.stdin.readline


def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)


n = int(input())
arr = list(map(int, input().split()))
k = int(input())

dfs(k, arr)
cnt = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        cnt += 1
print(cnt)
